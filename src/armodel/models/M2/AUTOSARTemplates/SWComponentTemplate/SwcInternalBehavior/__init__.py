from typing import List, Optional, cast

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ApiPrincipleEnum, InternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import PerInstanceMemory
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    AsynchronousServerCallReturnsEvent,
    BackgroundEvent,
    DataReceiveErrorEvent,
    ExternalTriggerOccurredEvent as ExternalTriggerOccurredEvent,
    OsTaskExecutionEvent as OsTaskExecutionEvent,
    TransformerHardErrorEvent as TransformerHardErrorEvent,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataSendCompletedEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataWriteCompletedEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import ModeSwitchedAckEvent, OperationInvokedEvent, RTEEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import SwcModeSwitchEvent, TimingEvent, WaitPoint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    CIdentifier,
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
    A RunnableEntity represents the smallest code-fragment that is provided by an AtomicSwComponent Type and are executed under control of the RTE. RunnableEntities are for instance set up to respond to data reception or operation invocation on a server.
    """

    # RunnableEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.3, p.528
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] _createVariableAccess [x] impl  [—] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addArgument [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArguments [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createAsynchronousServerCallResultPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAsynchronousServerCallResultPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getCanBeInvokedConcurrently [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCanBeInvokedConcurrently [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataReadAccess [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataReadAccesses [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDataReceivePointByArgument [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataReceivePointByArguments [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDataReceivePointByValue [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataReceivePointByValues [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDataSendPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataSendPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createDataWriteAccess [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataWriteAccesses [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addExternalTriggeringPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getExternalTriggeringPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createInternalTriggeringPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInternalTriggeringPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModeAccessPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeAccessPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createModeSwitchPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeSwitchPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createParameterAccess [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParameterAccesses [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createReadLocalVariable [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getReadLocalVariables [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createAsynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAsynchronousServerCallPoint [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getServerCallPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSymbol [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSymbol [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createWaitPoint [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWaitPoints [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createWrittenLocalVariable [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWrittenLocalVariables [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the formal definition of a an argument to a RunnableEntity.
        self.arguments: List[RunnableEntityArgument] = []

        # The server call result point admits a runnable to fetch the result of an asynchronous server call. The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=asynchronousServerCallResultPoint.short Name, asynchronousServerCallResultPoint.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.asynchronousServerCallResultPoints: List[AsynchronousServerCallResultPoint] = []

        # If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponent Type). This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency.
        self.canBeInvokedConcurrently: Optional[Boolean] = None

        # RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReadAccess.shortName, dataRead Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataReadAccesses: List[VariableAccess] = []

        # RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of an argument in the function signature. The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByArgument.shortName, dataReceivePointByArgument.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataReceivePointByArguments: List[VariableAccess] = []

        # RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of the return value. The aggregation of dataReceivePointBy Value is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByValue.shortName, data ReceivePointByValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataReceivePointByValues: List[VariableAccess] = []

        # RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataSendPoint.shortName, dataSend Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataSendPoints: List[VariableAccess] = []

        # RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataWriteAccess.shortName, dataWrite Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.dataWriteAccesses: List[VariableAccess] = []

        # The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=externalTriggeringPoint.ident.shortName, externalTriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.externalTriggeringPoints: List[ExternalTriggeringPoint] = []

        # The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=internalTriggeringPoint.shortName, internal TriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.internalTriggeringPoints: List[InternalTriggeringPoint] = []

        # The runnable has a mode access point. The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeAccessPoint.ident.shortName, mode AccessPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.modeAccessPoints: List[ModeAccessPoint] = []

        # The runnable has a mode switch point. The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchPoint.shortName, modeSwitch Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.modeSwitchPoints: List[ModeSwitchPoint] = []

        # The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a Parameter DataPrototype which may either be local or within a Port Prototype. The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of Parameter Access (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=parameterAccess.shortName, parameter Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.parameterAccesses: List[ParameterAccess] = []

        # The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of read LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=readLocalVariable.shortName, readLocal Variable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.readLocalVariables: List[VariableAccess] = []

        # The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.serverCallPoints: List[ServerCallPoint] = []

        # The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase.
        self.symbol: Optional[CIdentifier] = None

        # The WaitPoint associated with the RunnableEntity.
        self.waitPoints: List[WaitPoint] = []

        # The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of written LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=writtenLocalVariable.shortName, written LocalVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.writtenLocalVariables: List[VariableAccess] = []

    def _createVariableAccess(self, short_name, variable_accesses: List[VariableAccess]):
        if not self.IsReferrableElementExists(short_name, VariableAccess):
            variable_access = VariableAccess(self, short_name)
            self.addReferrableElement(variable_access)
            variable_accesses.append(variable_access)
        return cast(VariableAccess, self.getReferrableElement(short_name, VariableAccess))

    def addArgument(self, value: Optional[RunnableEntityArgument]) -> "RunnableEntity":
        """
        This represents the formal definition of a an argument to a RunnableEntity.

        A None value is a no-op and does not append to arguments.
        """

        if value is not None:
            self.arguments.append(value)
        return self

    def getArguments(self) -> List[RunnableEntityArgument]:
        """
        This represents the formal definition of a an argument to a RunnableEntity.
        """

        return self.arguments

    def createAsynchronousServerCallResultPoint(self, short_name: str) -> AsynchronousServerCallResultPoint:
        """
        The server call result point admits a runnable to fetch the result of an asynchronous server call. The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=asynchronousServerCallResultPoint.short Name, asynchronousServerCallResultPoint.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """

        if not self.IsReferrableElementExists(short_name, AsynchronousServerCallResultPoint):
            point = AsynchronousServerCallResultPoint(self, short_name)
            self.addReferrableElement(point)
            self.asynchronousServerCallResultPoints.append(point)
        return cast(AsynchronousServerCallResultPoint, self.getReferrableElement(short_name, AsynchronousServerCallResultPoint))

    def getAsynchronousServerCallResultPoints(self) -> List[AsynchronousServerCallResultPoint]:
        """
        The server call result point admits a runnable to fetch the result of an asynchronous server call. The aggregation of AsynchronousServerCallResultPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes and the variant existence of server call result points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=asynchronousServerCallResultPoint.short Name, asynchronousServerCallResultPoint.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.asynchronousServerCallResultPoints

    def getCanBeInvokedConcurrently(self) -> Optional[Boolean]:
        """
        If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponent Type). This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency.
        """

        return self.canBeInvokedConcurrently

    def setCanBeInvokedConcurrently(self, value: Optional[Boolean]) -> "RunnableEntity":
        """
        If the value of this attribute is set to "true" the enclosing RunnableEntity can be invoked concurrently (even for one instance of the corresponding AtomicSwComponent Type). This implies that it is the responsibility of the implementation of the RunnableEntity to take care of this form of concurrency.

        A None value is a no-op and does not overwrite an existing canBeInvokedConcurrently.
        """

        if value is not None:
            self.canBeInvokedConcurrently = value
        return self

    def createDataReadAccess(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReadAccess.shortName, dataRead Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.dataReadAccesses)

    def getDataReadAccesses(self) -> List[VariableAccess]:
        """
        RunnableEntity has implicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataReadAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataReadAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReadAccess.shortName, dataRead Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.dataReadAccesses

    def createDataReceivePointByArgument(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of an argument in the function signature. The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByArgument.shortName, dataReceivePointByArgument.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.dataReceivePointByArguments)

    def getDataReceivePointByArguments(self) -> List[VariableAccess]:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of an argument in the function signature. The aggregation of dataReceivePointByArgument is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByArgument.shortName, dataReceivePointByArgument.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.dataReceivePointByArguments

    def createDataReceivePointByValue(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of the return value. The aggregation of dataReceivePointBy Value is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByValue.shortName, data ReceivePointByValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.dataReceivePointByValues)

    def getDataReceivePointByValues(self) -> List[VariableAccess]:
        """
        RunnableEntity has explicit read access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The result is passed back to the application by means of the return value. The aggregation of dataReceivePointBy Value is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of data receive points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataReceivePointByValue.shortName, data ReceivePointByValue.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.dataReceivePointByValues

    def createDataSendPoint(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataSendPoint.shortName, dataSend Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.dataSendPoints)

    def getDataSendPoints(self) -> List[VariableAccess]:
        """
        RunnableEntity has explicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataSendPoint is subject to variability with the purpose to support the conditional existence of sender receiver PortPrototype or the variant existence of data send points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataSendPoint.shortName, dataSend Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.dataSendPoints

    def createDataWriteAccess(self, short_name: str) -> VariableAccess:
        """
        RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataWriteAccess.shortName, dataWrite Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.dataWriteAccesses)

    def getDataWriteAccesses(self) -> List[VariableAccess]:
        """
        RunnableEntity has implicit write access to dataElement of a sender-receiver PortPrototype or nv data of a nv data PortPrototype. The aggregation of dataWriteAccess is subject to variability with the purpose to support the conditional existence of sender receiver ports or the variant existence of dataWriteAccess in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataWriteAccess.shortName, dataWrite Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.dataWriteAccesses

    def addExternalTriggeringPoint(self, value: Optional[ExternalTriggeringPoint]) -> "RunnableEntity":
        """
        The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=externalTriggeringPoint.ident.shortName, externalTriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not append to externalTriggeringPoints.
        """

        if value is not None:
            self.externalTriggeringPoints.append(value)
        return self

    def getExternalTriggeringPoints(self) -> List[ExternalTriggeringPoint]:
        """
        The aggregation of ExternalTriggeringPoint is subject to variability with the purpose to support the conditional existence of trigger ports or the variant existence of external triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=externalTriggeringPoint.ident.shortName, externalTriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.externalTriggeringPoints

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        """
        The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=internalTriggeringPoint.shortName, internal TriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        if not self.IsReferrableElementExists(short_name, InternalTriggeringPoint):
            point = InternalTriggeringPoint(self, short_name)
            self.addReferrableElement(point)
            self.internalTriggeringPoints.append(point)
        return cast(InternalTriggeringPoint, self.getReferrableElement(short_name, InternalTriggeringPoint))

    def getInternalTriggeringPoints(self) -> List[InternalTriggeringPoint]:
        """
        The aggregation of InternalTriggeringPoint is subject to variability with the purpose to support the variant existence of internal triggering points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=internalTriggeringPoint.shortName, internal TriggeringPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.internalTriggeringPoints

    def addModeAccessPoint(self, value: Optional[ModeAccessPoint]) -> "RunnableEntity":
        """
        The runnable has a mode access point. The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeAccessPoint.ident.shortName, mode AccessPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not append to modeAccessPoints.
        """

        if value is not None:
            self.modeAccessPoints.append(value)
        return self

    def getModeAccessPoints(self) -> List[ModeAccessPoint]:
        """
        The runnable has a mode access point. The aggregation of ModeAccessPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode access points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeAccessPoint.ident.shortName, mode AccessPoint.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.modeAccessPoints

    def createModeSwitchPoint(self, short_name: str) -> ModeSwitchPoint:
        """
        The runnable has a mode switch point. The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchPoint.shortName, modeSwitch Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        if not self.IsReferrableElementExists(short_name, ModeSwitchPoint):
            point = ModeSwitchPoint(self, short_name)
            self.addReferrableElement(point)
            self.modeSwitchPoints.append(point)
        return cast(ModeSwitchPoint, self.getReferrableElement(short_name, ModeSwitchPoint))

    def getModeSwitchPoints(self) -> List[ModeSwitchPoint]:
        """
        The runnable has a mode switch point. The aggregation of ModeSwitchPoint is subject to variability with the purpose to support the conditional existence of mode ports or the variant existence of mode switch points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=modeSwitchPoint.shortName, modeSwitch Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.modeSwitchPoints

    def createParameterAccess(self, short_name: str) -> ParameterAccess:
        """
        The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a Parameter DataPrototype which may either be local or within a Port Prototype. The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of Parameter Access (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=parameterAccess.shortName, parameter Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        if not self.IsReferrableElementExists(short_name, ParameterAccess):
            access = ParameterAccess(self, short_name)
            self.addReferrableElement(access)
            self.parameterAccesses.append(access)
        return cast(ParameterAccess, self.getReferrableElement(short_name, ParameterAccess))

    def getParameterAccesses(self) -> List[ParameterAccess]:
        """
        The presence of a ParameterAccess implies that a RunnableEntity needs read only access to a Parameter DataPrototype which may either be local or within a Port Prototype. The aggregation of ParameterAccess is subject to variability with the purpose to support the conditional existence of parameter ports and component local parameters as well as the variant existence of Parameter Access (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=parameterAccess.shortName, parameter Access.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.parameterAccesses

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        """
        The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of read LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=readLocalVariable.shortName, readLocal Variable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.readLocalVariables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
        """
        The presence of a readLocalVariable implies that a RunnableEntity needs read access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of readLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of read LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=readLocalVariable.shortName, readLocal Variable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.readLocalVariables

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        """
        The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        if not self.IsReferrableElementExists(short_name, AsynchronousServerCallPoint):
            point = AsynchronousServerCallPoint(self, short_name)
            self.addReferrableElement(point)
            self.serverCallPoints.append(point)
        return cast(AsynchronousServerCallPoint, self.getReferrableElement(short_name, AsynchronousServerCallPoint))

    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        """
        The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        if not self.IsReferrableElementExists(short_name, SynchronousServerCallPoint):
            point = SynchronousServerCallPoint(self, short_name)
            self.addReferrableElement(point)
            self.serverCallPoints.append(point)
        return cast(SynchronousServerCallPoint, self.getReferrableElement(short_name, SynchronousServerCallPoint))

    def getSynchronousServerCallPoint(self) -> List[SynchronousServerCallPoint]:
        """
        The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return [point for point in self.serverCallPoints if isinstance(point, SynchronousServerCallPoint)]

    def getAsynchronousServerCallPoint(self) -> List[AsynchronousServerCallPoint]:
        """
        The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return [point for point in self.serverCallPoints if isinstance(point, AsynchronousServerCallPoint)]

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        """
        The RunnableEntity has a ServerCallPoint. The aggregation of ServerCallPoint is subject to variability with the purpose to support the conditional existence of client server PortPrototypes or the variant existence of server call points in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serverCallPoint.shortName, serverCall Point.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.serverCallPoints

    def getSymbol(self) -> Optional[CIdentifier]:
        """
        The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase.
        """

        return self.symbol

    def setSymbol(self, value: Optional[CIdentifier]) -> "RunnableEntity":
        """
        The symbol describing this RunnableEntity's entry point. This is considered the API of the RunnableEntity and is required during the RTE contract phase.

        A None value is a no-op and does not overwrite an existing symbol.
        """

        if value is not None:
            self.symbol = value
        return self

    def createWaitPoint(self, short_name: str) -> WaitPoint:
        """
        The WaitPoint associated with the RunnableEntity.
        """

        if not self.IsReferrableElementExists(short_name, WaitPoint):
            point = WaitPoint(self, short_name)
            self.addReferrableElement(point)
            self.waitPoints.append(point)
        return cast(WaitPoint, self.getReferrableElement(short_name, WaitPoint))

    def getWaitPoints(self) -> List[WaitPoint]:
        """
        The WaitPoint associated with the RunnableEntity.
        """

        return self.waitPoints

    def createWrittenLocalVariable(self, short_name: str) -> VariableAccess:
        """
        The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of written LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=writtenLocalVariable.shortName, written LocalVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self._createVariableAccess(short_name, self.writtenLocalVariables)

    def getWrittenLocalVariables(self) -> List[VariableAccess]:
        """
        The presence of a writtenLocalVariable implies that a RunnableEntity needs write access to a VariableData Prototype in the role of implicitInterRunnableVariable or explicitInterRunnableVariable. The aggregation of writtenLocalVariable is subject to variability with the purpose to support the conditional existence of implicitInterRunnableVariable and explicit InterRunnableVariable or the variant existence of written LocalVariable (points) in the implementation. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=writtenLocalVariable.shortName, written LocalVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """

        return self.writtenLocalVariables


class SwcExclusiveAreaPolicy(ARObject, VariationPointCapable):
    """
    Options how to generate the ExclusiveArea related APIs. If no SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values apply.
    """

    # SwcExclusiveAreaPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.28, p.556
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApiPrinciple             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setApiPrinciple             [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getExclusiveAreaRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setExclusiveAreaRef         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies for this ExclusiveArea if either one common set of Enter and Exit APIs for the whole software component is requested from the Rte or if the set of Enter and Exit APIs is expected per RunnableEntity. The default value is "common".
        self.apiPrinciple: Optional[ApiPrincipleEnum] = None

        # This reference represents the ExclusiveArea for which the policy applies.
        self.exclusiveAreaRef: Optional[RefType] = None

    def getApiPrinciple(self) -> Optional[ApiPrincipleEnum]:
        """
        Specifies for this ExclusiveArea if either one common set of Enter and Exit APIs for the whole software component is requested from the Rte or if the set of Enter and Exit APIs is expected per RunnableEntity. The default value is "common".
        """
        return self.apiPrinciple

    def setApiPrinciple(self, value: Optional[ApiPrincipleEnum]) -> "SwcExclusiveAreaPolicy":
        """
        Specifies for this ExclusiveArea if either one common set of Enter and Exit APIs for the whole software component is requested from the Rte or if the set of Enter and Exit APIs is expected per RunnableEntity. The default value is "common".
        A None value is a no-op and does not overwrite an existing apiPrinciple.
        """
        if value is not None:
            self.apiPrinciple = value
        return self

    def getExclusiveAreaRef(self) -> Optional[RefType]:
        """
        This reference represents the ExclusiveArea for which the policy applies.
        """
        return self.exclusiveAreaRef

    def setExclusiveAreaRef(self, value: Optional[RefType]) -> "SwcExclusiveAreaPolicy":
        """
        This reference represents the ExclusiveArea for which the policy applies.
        A None value is a no-op and does not overwrite an existing exclusiveAreaRef.
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
    # [x] createDataReceiveErrorEvent                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSwcModeSwitchEvent                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createInternalTriggerOccurredEvent           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createModeSwitchedAckEvent                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createBackgroundEvent                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataSendCompletedEvent                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createDataWriteCompletedEvent                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createExternalTriggerOccurredEvent           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
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
    # [x] getExternalTriggerOccurredEvents             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
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
        if not self.IsReferrableElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.arTypedPerInstanceMemories.append(prototype)
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """
        Implement state message semantics for establishing communication among runnables of the same component. The aggregation of explicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=explicitInterRunnableVariable.shortName, explicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.explicitInterRunnableVariables

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """
        Implement state message semantics for establishing communication among runnables of the same component. The aggregation of explicitInterRunnable Variable is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=explicitInterRunnableVariable.shortName, explicitInterRunnableVariable.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.explicitInterRunnableVariables.append(prototype)
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

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
        if not self.IsReferrableElementExists(short_name, VariableDataPrototype):
            prototype = VariableDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.implicitInterRunnableVariables.append(prototype)
        return cast(VariableDataPrototype, self.getReferrableElement(short_name, VariableDataPrototype))

    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        """
        Defines a per-instance memory object needed by this software component. The aggregation of PerInstance Memory is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceMemory.shortName, perInstance Memory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.perInstanceMemories

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        """
        Defines a per-instance memory object needed by this software component. The aggregation of PerInstance Memory is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceMemory.shortName, perInstance Memory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, PerInstanceMemory):
            memory = PerInstanceMemory(self, short_name)
            self.addReferrableElement(memory)
            self.perInstanceMemories.append(memory)
        return cast(PerInstanceMemory, self.getReferrableElement(short_name, PerInstanceMemory))

    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        """
        Defines parameter(s) or characteristic value(s) that needs to be available for each instance of the software-component. This is typically only useful if supportsMultipleInstantiation is set to "true". The aggregation of perInstanceParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceParameter.shortName, per InstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.perInstanceParameters

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        """
        Defines parameter(s) or characteristic value(s) that needs to be available for each instance of the software-component. This is typically only useful if supportsMultipleInstantiation is set to "true". The aggregation of perInstanceParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=perInstanceParameter.shortName, per InstanceParameter.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, ParameterDataPrototype):
            prototype = ParameterDataPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.perInstanceParameters.append(prototype)
        return cast(ParameterDataPrototype, self.getReferrableElement(short_name, ParameterDataPrototype))

    def getSharedParameters(self) -> List[ParameterDataPrototype]:
        """
        Defines parameter(s) or characteristic value(s) shared between SwComponentPrototypes of the same Sw ComponentType The aggregation of sharedParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sharedParameter.shortName, shared Parameter.variationPoint.shortLabel
        """
        return self.sharedParameters

    def createSharedParameter(self, short_name: str) -> ParameterDataPrototype:
        """
        Defines parameter(s) or characteristic value(s) shared between SwComponentPrototypes of the same Sw ComponentType The aggregation of sharedParameter is subject to variability with the purpose to support variability in the software components implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sharedParameter.shortName, shared Parameter.variationPoint.shortLabel
        """
        if not self.IsReferrableElementExists(short_name, ParameterDataPrototype):
            memory = ParameterDataPrototype(self, short_name)
            self.addReferrableElement(memory)
            self.sharedParameters.append(memory)
        return cast(ParameterDataPrototype, self.getReferrableElement(short_name, ParameterDataPrototype))

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
        if not self.IsReferrableElementExists(short_name, OperationInvokedEvent):
            event = OperationInvokedEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(OperationInvokedEvent, self.getReferrableElement(short_name, OperationInvokedEvent))

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, TimingEvent):
            event = TimingEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(TimingEvent, self.getReferrableElement(short_name, TimingEvent))

    def createInitEvent(self, short_name: str) -> InitEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, InitEvent):
            event = InitEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(InitEvent, self.getReferrableElement(short_name, InitEvent))

    def createAsynchronousServerCallReturnsEvent(self, short_name: str) -> AsynchronousServerCallReturnsEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, AsynchronousServerCallReturnsEvent):
            event = AsynchronousServerCallReturnsEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(AsynchronousServerCallReturnsEvent, self.getReferrableElement(short_name, AsynchronousServerCallReturnsEvent))

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, DataReceivedEvent):
            event = DataReceivedEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(DataReceivedEvent, self.getReferrableElement(short_name, DataReceivedEvent))

    def createDataReceiveErrorEvent(self, short_name: str) -> DataReceiveErrorEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, DataReceiveErrorEvent):
            event = DataReceiveErrorEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(DataReceiveErrorEvent, self.getReferrableElement(short_name, DataReceiveErrorEvent))

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, SwcModeSwitchEvent):
            event = SwcModeSwitchEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(SwcModeSwitchEvent, self.getReferrableElement(short_name, SwcModeSwitchEvent))

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, InternalTriggerOccurredEvent):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(InternalTriggerOccurredEvent, self.getReferrableElement(short_name, InternalTriggerOccurredEvent))

    def createModeSwitchedAckEvent(self, short_name: str) -> ModeSwitchedAckEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, ModeSwitchedAckEvent):
            event = ModeSwitchedAckEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(ModeSwitchedAckEvent, self.getReferrableElement(short_name, ModeSwitchedAckEvent))

    def createBackgroundEvent(self, short_name: str) -> BackgroundEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, BackgroundEvent):
            event = BackgroundEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(BackgroundEvent, self.getReferrableElement(short_name, BackgroundEvent))

    def createDataSendCompletedEvent(self, short_name: str) -> DataSendCompletedEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, DataSendCompletedEvent):
            event = DataSendCompletedEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(DataSendCompletedEvent, self.getReferrableElement(short_name, DataSendCompletedEvent))

    def createDataWriteCompletedEvent(self, short_name: str) -> DataWriteCompletedEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, DataWriteCompletedEvent):
            event = DataWriteCompletedEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(DataWriteCompletedEvent, self.getReferrableElement(short_name, DataWriteCompletedEvent))

    def createExternalTriggerOccurredEvent(self, short_name: str) -> ExternalTriggerOccurredEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, ExternalTriggerOccurredEvent):
            event = ExternalTriggerOccurredEvent(self, short_name)
            self.addReferrableElement(event)
            self.events.append(event)
        return cast(ExternalTriggerOccurredEvent, self.getReferrableElement(short_name, ExternalTriggerOccurredEvent))

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation of SwcServiceDependency is subject to variability with the purpose to support the conditional existence of ports as well as the conditional existence of ServiceNeeds. The SwcServiceDependency owned by an SwcInternal Behavior can be located in a different physical file in order to support that SwcServiceDependency might be provided in later development steps or even by different expert domain (e.g OBD expert for Obd related Service Needs) tools. Therefore the aggregation is <<atp Splitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceDependency.shortName, service Dependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, SwcServiceDependency):
            event = SwcServiceDependency(self, short_name)
            self.addReferrableElement(event)
            self.serviceDependencies.append(event)
        return cast(SwcServiceDependency, self.getReferrableElement(short_name, SwcServiceDependency))

    def getRteEvents(self) -> List[RTEEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted(self.events, key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, OperationInvokedEvent)], key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, InitEvent)], key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, TimingEvent)], key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, DataReceivedEvent)], key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, SwcModeSwitchEvent)], key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, InternalTriggerOccurredEvent)], key=lambda e: e.short_name)

    def getModeSwitchedAckEvents(self) -> List[ModeSwitchedAckEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, ModeSwitchedAckEvent)], key=lambda e: e.short_name)

    def getBackgroundEvents(self) -> List[BackgroundEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, BackgroundEvent)], key=lambda e: e.short_name)

    def getDataSendCompletedEvents(self) -> List[DataSendCompletedEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, DataSendCompletedEvent)], key=lambda e: e.short_name)

    def getExternalTriggerOccurredEvents(self) -> List[ExternalTriggerOccurredEvent]:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return sorted([c for c in self.events if isinstance(c, ExternalTriggerOccurredEvent)], key=lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        """
        Defines the requirements on AUTOSAR Services for a particular item. The aggregation of SwcServiceDependency is subject to variability with the purpose to support the conditional existence of ports as well as the conditional existence of ServiceNeeds. The SwcServiceDependency owned by an SwcInternal Behavior can be located in a different physical file in order to support that SwcServiceDependency might be provided in later development steps or even by different expert domain (e.g OBD expert for Obd related Service Needs) tools. Therefore the aggregation is <<atp Splitable>>. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=serviceDependency.shortName, service Dependency.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return sorted(self.serviceDependencies, key=lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        """
        This is a RTEEvent specified for the particular Swc InternalBehavior. The aggregation of RTEEvent is subject to variability with the purpose to support the conditional existence of RTE events. Note: the number of RTE events might vary due to the conditional existence of PortPrototypes using Data ReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=event.shortName, event.variationPoint.short Label vh.latestBindingTime=preCompileTime
        """
        return cast(RTEEvent, self.getReferrableElement(short_name, RTEEvent))

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        """Gets all VariableDataPrototype instances owned by this behavior, sorted by short name."""
        return sorted([c for c in self.referrableElements if isinstance(c, VariableDataPrototype)], key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        """
        This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, RunnableEntity):
            runnable = RunnableEntity(self, short_name)
            self.addReferrableElement(runnable)
            self.runnables.append(runnable)
        return cast(RunnableEntity, self.getReferrableElement(short_name, RunnableEntity))

    def getRunnableEntities(self) -> List[RunnableEntity]:
        """
        This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        return sorted(self.runnables, key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name: str) -> RunnableEntity:
        """
        This is a RunnableEntity specified for the particular Swc InternalBehavior. The aggregation of RunnableEntity is subject to variability with the purpose to support the conditional existence of RunnableEntities. Note: the number of RunnableEntities might vary due to the conditional existence of Port Prototypes using DataReceivedEvents or due to different scheduling needs of algorithms. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runnable.shortName, runnable.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        """
        return cast(RunnableEntity, self.getReferrableElement(short_name, RunnableEntity))

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
