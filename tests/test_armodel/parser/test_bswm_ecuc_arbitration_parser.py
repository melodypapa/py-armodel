from pathlib import Path

import pytest

from armodel.data_models.ecuc import BswmModule
from armodel.parser import BswmEcucParser
from armodel.parser.bswm_ecuc_parser import BSWM_EVENT_REQUEST_SOURCES, BSWM_GENERAL_PARAMETERS, BSWM_MODE_REQUEST_SOURCES

FIXTURE = Path(__file__).parent / "data" / "bswm_ecuc_arbitration.arxml"
ARB = "/Vendor/BswM/BswMConfig_0/BswMArbitration/"
CTRL = "/Vendor/BswM/BswMConfig_0/BswMModeControl/"


@pytest.fixture(scope="module")
def module() -> BswmModule:
    return BswmEcucParser().load(str(FIXTURE), warning=False)


def test_sws_tables_match_chapter_10_2():
    assert len(BSWM_MODE_REQUEST_SOURCES) == 27
    assert BSWM_MODE_REQUEST_SOURCES["BswMLinScheduleIndication"] == ["BswMLinScheduleRef", "BswMLinSMChannelRef"]
    assert BSWM_MODE_REQUEST_SOURCES["BswMTimer"] == []
    assert len(BSWM_EVENT_REQUEST_SOURCES) == 6
    assert BSWM_EVENT_REQUEST_SOURCES["BswMSwitchAckNotification"] == ["BswMSwitchPortRef"]
    assert len(BSWM_GENERAL_PARAMETERS) == 19


def test_rule_fields_and_references(module: BswmModule):
    [rule] = module.getRules()

    assert rule.getName() == "R_CAN1"
    assert (rule.getNestedExecutionOnly(), rule.getInitState()) == (False, "BSWM_UNDEFINED")
    assert (rule.getExpressionRef(), rule.getTrueActionList(), rule.getFalseActionList()) == (ARB + "LE_Outer", CTRL + "AL_Startup", None)


def test_logical_expressions_resolve_argument_types(module: BswmModule):
    expressions = {expression.getName(): expression for expression in module.getLogicalExpressions()}

    assert expressions["LE_CAN1"].getOperator() == "BSWM_NOT"
    assert expressions["LE_CAN1"].getArgumentRefs() == [ARB + "MC_CAN1_FULL", ARB + "MC_Reset"]
    assert expressions["LE_CAN1"].getArgumentRefTypes() == ["BswMModeCondition", "BswMModeCondition"]
    assert expressions["LE_Outer"].getArgumentRefTypes() == ["BswMLogicalExpression"]


def test_mode_conditions_read_type_port_kind_and_value_choice(module: BswmModule):
    conditions = {condition.getName(): condition for condition in module.getModeConditions()}

    full = conditions["MC_CAN1_FULL"]
    assert (full.getConditionType(), full.getConditionModeType(), full.getConditionValueType()) == ("BSWM_EQUALS", "BswMModeRequestPort", "BswMBswMode")
    assert full.getConditionValue("BswMBswRequestedMode") == ["COMM_FULL_COMMUNICATION"]
    reset = conditions["MC_Reset"]
    assert (reset.getConditionModeType(), reset.getConditionValueType(), reset.getConditionValues()) == ("BswMEventRequestPort", None, {})


def test_request_ports_keep_only_sws_source_parameters(module: BswmModule):
    [mode_port] = module.getModeRequestPorts()
    [event_port] = module.getEventRequestPorts()

    assert (mode_port.getName(), mode_port.getRequestProcessing(), mode_port.getSourceType()) == ("MRP_ComM_CAN1", "BSWM_IMMEDIATE", "BswMComMIndication")
    assert mode_port.getSourceParameters() == {"BswMComMChannelRef": ["/Vendor/ComM/ComMConfigSet/CAN1"]}
    assert mode_port.getBswModeInitValue() == "COMM_NO_COMMUNICATION"
    assert (event_port.getName(), event_port.getRequestProcessing(), event_port.getSourceType(), event_port.getSourceParameters()) == ("ERP_ComMReset", "BSWM_DEFERRED", "BswMComMInitiateReset", {})


def test_switch_port_general_and_rule_items(module: BswmModule):
    [switch_port] = module.getSwitchPorts()
    general = module.getGeneral()
    [action_list] = module.getActionLists()

    assert (switch_port.getName(), switch_port.getModeSwitchInterfaceRef()) == ("SP_AppMode", "/Vendor/Interfaces/AppModeIf")
    assert general is not None
    assert general.getParameters() == {"BswMComMEnabled": True, "BswMMainFunctionPeriod": 0.01}
    assert general.getUserIncludeFiles() == ["App.h", "Diag.h"]
    assert [(item.getName(), item.getActionRefType(), item.getReportFailRuntimeErrorId()) for item in action_list.getItems()] == [("AI_Switch", "BswMAction", 300), ("AI_Nested", "BswMRule", None)]
