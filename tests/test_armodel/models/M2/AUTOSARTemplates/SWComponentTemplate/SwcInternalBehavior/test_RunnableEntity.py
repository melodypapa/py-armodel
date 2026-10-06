import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CIdentifier
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import RunnableEntity
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeAccessPoint, ModeSwitchPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import WaitPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntityArgument import RunnableEntityArgument
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    AsynchronousServerCallPoint,
    AsynchronousServerCallResultPoint,
    SynchronousServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import ExternalTriggeringPoint, InternalTriggeringPoint


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_runnable():
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("Behavior")
    return behavior.createRunnableEntity("Cyclic")


class TestRunnableEntity:
    def test_initialization_defaults(self):
        runnable = _make_runnable()
        assert isinstance(runnable, RunnableEntity)
        assert runnable.arguments == []
        assert runnable.asynchronousServerCallResultPoints == []
        assert runnable.canBeInvokedConcurrently is None
        assert runnable.dataReadAccesses == []
        assert runnable.dataReceivePointByArguments == []
        assert runnable.dataReceivePointByValues == []
        assert runnable.dataSendPoints == []
        assert runnable.dataWriteAccesses == []
        assert runnable.externalTriggeringPoints == []
        assert runnable.internalTriggeringPoints == []
        assert runnable.modeAccessPoints == []
        assert runnable.modeSwitchPoints == []
        assert runnable.parameterAccesses == []
        assert runnable.readLocalVariables == []
        assert runnable.serverCallPoints == []
        assert runnable.symbol is None
        assert runnable.waitPoints == []
        assert runnable.writtenLocalVariables == []

    def test_class_docstring_is_spec_note_verbatim(self):
        assert (
            inspect.getdoc(RunnableEntity)
            == "A RunnableEntity represents the smallest code-fragment that is provided by an AtomicSwComponent Type and are executed under control of the RTE. RunnableEntities are for instance set up to respond to data reception or operation invocation on a server."
        )

    def test_add_get_arguments(self):
        runnable = _make_runnable()
        argument = RunnableEntityArgument()
        assert runnable.addArgument(argument) is runnable
        assert runnable.getArguments() is runnable.arguments
        assert runnable.getArguments() == [argument]
        runnable.addArgument(None)
        assert runnable.getArguments() == [argument]

    def test_getters_return_dedicated_fields(self):
        runnable = _make_runnable()
        assert runnable.getArguments() is runnable.arguments
        assert runnable.getAsynchronousServerCallResultPoints() is runnable.asynchronousServerCallResultPoints
        assert runnable.getDataReadAccesses() is runnable.dataReadAccesses
        assert runnable.getDataReceivePointByArguments() is runnable.dataReceivePointByArguments
        assert runnable.getDataReceivePointByValues() is runnable.dataReceivePointByValues
        assert runnable.getDataSendPoints() is runnable.dataSendPoints
        assert runnable.getDataWriteAccesses() is runnable.dataWriteAccesses
        assert runnable.getExternalTriggeringPoints() is runnable.externalTriggeringPoints
        assert runnable.getInternalTriggeringPoints() is runnable.internalTriggeringPoints
        assert runnable.getModeAccessPoints() is runnable.modeAccessPoints
        assert runnable.getModeSwitchPoints() is runnable.modeSwitchPoints
        assert runnable.getParameterAccesses() is runnable.parameterAccesses
        assert runnable.getReadLocalVariables() is runnable.readLocalVariables
        assert runnable.getServerCallPoints() is runnable.serverCallPoints
        assert runnable.getWaitPoints() is runnable.waitPoints
        assert runnable.getWrittenLocalVariables() is runnable.writtenLocalVariables

    def test_get_set_can_be_invoked_concurrently(self):
        runnable = _make_runnable()
        value = Boolean().setValue("true")
        assert runnable.setCanBeInvokedConcurrently(value) is runnable
        assert runnable.getCanBeInvokedConcurrently() is value
        runnable.setCanBeInvokedConcurrently(None)
        assert runnable.getCanBeInvokedConcurrently() is value

    def test_create_variable_accesses_append_to_dedicated_fields(self):
        runnable = _make_runnable()
        read_access = runnable.createDataReadAccess("Read1")
        assert isinstance(read_access, VariableAccess)
        assert runnable.dataReadAccesses == [read_access]
        assert runnable.createDataReadAccess("Read1") is read_access

        write_access = runnable.createDataWriteAccess("Write1")
        assert runnable.dataWriteAccesses == [write_access]

        receive_by_arg = runnable.createDataReceivePointByArgument("RecvArg")
        assert runnable.dataReceivePointByArguments == [receive_by_arg]

        receive_by_value = runnable.createDataReceivePointByValue("RecvVal")
        assert runnable.dataReceivePointByValues == [receive_by_value]

        send_point = runnable.createDataSendPoint("Send1")
        assert runnable.dataSendPoints == [send_point]

        read_local = runnable.createReadLocalVariable("ReadLocal")
        assert runnable.readLocalVariables == [read_local]

        written_local = runnable.createWrittenLocalVariable("WrittenLocal")
        assert runnable.writtenLocalVariables == [written_local]

    def test_create_parameter_access_appends_to_field(self):
        runnable = _make_runnable()
        access = runnable.createParameterAccess("ParamAccess1")
        assert isinstance(access, ParameterAccess)
        assert runnable.parameterAccesses == [access]
        assert runnable.getParameterAccesses() == [access]
        assert runnable.createParameterAccess("ParamAccess1") is access

    def test_create_server_call_points_append_to_field(self):
        runnable = _make_runnable()
        sync_point = runnable.createSynchronousServerCallPoint("Sync1")
        assert isinstance(sync_point, SynchronousServerCallPoint)
        assert runnable.serverCallPoints == [sync_point]

        async_point = runnable.createAsynchronousServerCallPoint("Async1")
        assert isinstance(async_point, AsynchronousServerCallPoint)
        assert runnable.serverCallPoints == [sync_point, async_point]

        assert runnable.createSynchronousServerCallPoint("Sync1") is sync_point
        assert runnable.createAsynchronousServerCallPoint("Async1") is async_point
        assert len(runnable.serverCallPoints) == 2
        assert runnable.getServerCallPoints() == [sync_point, async_point]

        sync_points = runnable.getSynchronousServerCallPoint()
        assert sync_points == [sync_point]
        async_points = runnable.getAsynchronousServerCallPoint()
        assert async_points == [async_point]

    def test_create_asynchronous_server_call_result_point_appends_to_field(self):
        runnable = _make_runnable()
        point = runnable.createAsynchronousServerCallResultPoint("Result1")
        assert isinstance(point, AsynchronousServerCallResultPoint)
        assert runnable.asynchronousServerCallResultPoints == [point]
        assert runnable.getAsynchronousServerCallResultPoints() == [point]
        assert runnable.createAsynchronousServerCallResultPoint("Result1") is point

    def test_add_get_external_triggering_points(self):
        runnable = _make_runnable()
        point = ExternalTriggeringPoint()
        assert runnable.addExternalTriggeringPoint(point) is runnable
        assert runnable.externalTriggeringPoints == [point]
        assert runnable.getExternalTriggeringPoints() == [point]
        runnable.addExternalTriggeringPoint(None)
        assert runnable.getExternalTriggeringPoints() == [point]

    def test_create_get_internal_triggering_points(self):
        runnable = _make_runnable()
        point = runnable.createInternalTriggeringPoint("InternalTrig")
        assert isinstance(point, InternalTriggeringPoint)
        assert runnable.internalTriggeringPoints == [point]
        assert runnable.getInternalTriggeringPoints() == [point]
        assert runnable.createInternalTriggeringPoint("InternalTrig") is point

    def test_add_get_mode_access_points(self):
        runnable = _make_runnable()
        point = ModeAccessPoint()
        assert runnable.addModeAccessPoint(point) is runnable
        assert runnable.modeAccessPoints == [point]
        assert runnable.getModeAccessPoints() == [point]
        runnable.addModeAccessPoint(None)
        assert runnable.getModeAccessPoints() == [point]

    def test_create_get_mode_switch_points(self):
        runnable = _make_runnable()
        point = runnable.createModeSwitchPoint("ModeSwitch1")
        assert isinstance(point, ModeSwitchPoint)
        assert runnable.modeSwitchPoints == [point]
        assert runnable.getModeSwitchPoints() == [point]
        assert runnable.createModeSwitchPoint("ModeSwitch1") is point

    def test_create_get_wait_points(self):
        runnable = _make_runnable()
        point = runnable.createWaitPoint("Wait1")
        assert isinstance(point, WaitPoint)
        assert runnable.waitPoints == [point]
        assert runnable.getWaitPoints() == [point]
        assert runnable.createWaitPoint("Wait1") is point

    def test_get_set_symbol(self):
        runnable = _make_runnable()
        symbol = CIdentifier()
        symbol.setValue("SWC_Cyclic_Cyclic")
        assert runnable.setSymbol(symbol) is runnable
        assert runnable.getSymbol() is symbol
        assert runnable.getSymbol().getValue() == "SWC_Cyclic_Cyclic"
        runnable.setSymbol(None)
        assert runnable.getSymbol() is symbol
