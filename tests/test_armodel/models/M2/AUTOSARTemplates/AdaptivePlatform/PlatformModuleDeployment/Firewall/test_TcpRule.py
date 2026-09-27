import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import TcpRule, TransportLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger

NUMBER_OF_PARALLEL_TCP_SESSIONS_NOTE = "This attribute defines the maximal number of TCP Sessions that are allowed to be established."
STATE_MANAGEMENT_BASED_ON_TCP_FLAGS_NOTE = "This attribute defines whether the StateManagement is based on TCP flags or not."
TIMEOUT_CHECK_NOTE = "This attribute defines the TCP Session timeout in seconds"


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _boolean(value):
    b = Boolean()
    b.setValue(value)
    return b


class TestTcpRule:
    def test_defaults_in_spec_displayed_order(self):
        obj = TcpRule()
        assert isinstance(obj, ARObject)
        assert isinstance(obj, TransportLayerRule)
        assert obj.getNumberOfParallelTcpSessions() is None
        assert obj.getStateManagementBasedOnTcpFlags() is None
        assert obj.getTimeoutCheck() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert TcpRule.__doc__.strip() == "Configuration of TCP filter rules. Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(TcpRule.getNumberOfParallelTcpSessions.__doc__) == NUMBER_OF_PARALLEL_TCP_SESSIONS_NOTE
        assert (
            inspect.cleandoc(TcpRule.setNumberOfParallelTcpSessions.__doc__)
            == NUMBER_OF_PARALLEL_TCP_SESSIONS_NOTE + "\nA None value is a no-op and does not overwrite an existing numberOfParallelTcpSessions."
        )
        assert inspect.cleandoc(TcpRule.getStateManagementBasedOnTcpFlags.__doc__) == STATE_MANAGEMENT_BASED_ON_TCP_FLAGS_NOTE
        assert (
            inspect.cleandoc(TcpRule.setStateManagementBasedOnTcpFlags.__doc__)
            == STATE_MANAGEMENT_BASED_ON_TCP_FLAGS_NOTE + "\nA None value is a no-op and does not overwrite an existing stateManagementBasedOnTcpFlags."
        )
        assert inspect.cleandoc(TcpRule.getTimeoutCheck.__doc__) == TIMEOUT_CHECK_NOTE
        assert inspect.cleandoc(TcpRule.setTimeoutCheck.__doc__) == TIMEOUT_CHECK_NOTE + "\nA None value is a no-op and does not overwrite an existing timeoutCheck."

    def test_get_set_round_trip_and_none_noop(self):
        obj = TcpRule()
        number_of_parallel_tcp_sessions = _pos_int(4)
        state_management_based_on_tcp_flags = _boolean(True)
        timeout_check = _pos_int(30)

        assert obj.setNumberOfParallelTcpSessions(number_of_parallel_tcp_sessions) is obj
        assert obj.setStateManagementBasedOnTcpFlags(state_management_based_on_tcp_flags) is obj
        assert obj.setTimeoutCheck(timeout_check) is obj

        assert obj.getNumberOfParallelTcpSessions() is number_of_parallel_tcp_sessions
        assert obj.getStateManagementBasedOnTcpFlags() is state_management_based_on_tcp_flags
        assert obj.getTimeoutCheck() is timeout_check

        obj.setNumberOfParallelTcpSessions(None)
        obj.setStateManagementBasedOnTcpFlags(None)
        obj.setTimeoutCheck(None)
        assert obj.getNumberOfParallelTcpSessions() is number_of_parallel_tcp_sessions
        assert obj.getStateManagementBasedOnTcpFlags() is state_management_based_on_tcp_flags
        assert obj.getTimeoutCheck() is timeout_check

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(TcpRule.setNumberOfParallelTcpSessions)
        assert hints["return"] is TcpRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(TcpRule.setStateManagementBasedOnTcpFlags)
        assert hints["return"] is TcpRule
        assert hints["value"] == Optional[Boolean]
        hints = typing.get_type_hints(TcpRule.setTimeoutCheck)
        assert hints["return"] is TcpRule
        assert hints["value"] == Optional[PositiveInteger]
