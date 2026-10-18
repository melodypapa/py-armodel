from armodel.data_models.ecuc import (
    BswmAction,
    BswmActionList,
    BswmActionListItem,
    BswmEventRequestPort,
    BswmGeneral,
    BswmLogicalExpression,
    BswmModeCondition,
    BswmModeRequestPort,
    BswmModule,
    BswmRule,
    BswmSwitchPort,
)


def test_bswm_action_collects_repeated_parameters_in_order():
    action = BswmAction()

    result = action.setName("AC_PduGroupSwitch").setActionType("BswMPduGroupSwitch").addParameter("BswMEnabledPduGroupRef", "/Com/Tx").addParameter("BswMEnabledPduGroupRef", "/Com/Rx")

    assert result is action
    assert action.getActionType() == "BswMPduGroupSwitch"
    assert action.getParameter("BswMEnabledPduGroupRef") == ["/Com/Tx", "/Com/Rx"]
    assert action.getParameter("missing") == []


def test_bswm_action_list_holds_items():
    item = BswmActionListItem().setName("AI_1").setIndex(10).setAbortOnFail(False).setActionRef("/BswM/C/AC_1").setActionRefType("BswMAction")
    action_list = BswmActionList().setName("AL_1").setExecution("BSWM_TRIGGER").addItem(item)

    assert action_list.getItems() == [item]
    assert (item.getIndex(), item.getAbortOnFail(), item.getActionRef(), item.getActionRefType()) == (10, False, "/BswM/C/AC_1", "BswMAction")


def test_bswm_module_defaults_and_independent_instances():
    first = BswmModule().setName("BswM").addAction(BswmAction().setName("AC_1")).addActionList(BswmActionList().setName("AL_1"))
    second = BswmModule()

    assert [action.getName() for action in first.getActions()] == ["AC_1"]
    assert [action_list.getName() for action_list in first.getActionLists()] == ["AL_1"]
    assert second.getActions() == [] and second.getActionLists() == []
    assert BswmAction().getParameters() == {} and BswmActionList().getItems() == []


def test_bswm_rule_and_logical_expression_hold_references():
    rule = BswmRule().setName("R_1").setNestedExecutionOnly(False).setInitState("BSWM_UNDEFINED").setExpressionRef("/B/C/A/LE_1").setTrueActionList("/B/C/M/AL_1")
    expression = BswmLogicalExpression().setName("LE_1").setOperator("BSWM_AND").addArgumentRef("/B/C/A/MC_1", "BswMModeCondition").addArgumentRef("/B/C/A/LE_2", "BswMLogicalExpression")

    assert (rule.getNestedExecutionOnly(), rule.getInitState(), rule.getExpressionRef(), rule.getTrueActionList(), rule.getFalseActionList()) == (
        False,
        "BSWM_UNDEFINED",
        "/B/C/A/LE_1",
        "/B/C/M/AL_1",
        None,
    )
    assert expression.getArgumentRefs() == ["/B/C/A/MC_1", "/B/C/A/LE_2"]
    assert expression.getArgumentRefTypes() == ["BswMModeCondition", "BswMLogicalExpression"]


def test_bswm_mode_condition_and_request_ports_keep_choice_values():
    condition = BswmModeCondition().setName("MC_1").setConditionType("BSWM_EQUALS").setConditionMode("/B/C/A/MRP_1").setConditionModeType("BswMModeRequestPort")
    condition.setConditionValueType("BswMBswMode").addConditionValue("BswMBswRequestedMode", "COMM_FULL_COMMUNICATION")
    mode_port = (
        BswmModeRequestPort()
        .setName("MRP_1")
        .setRequestProcessing("BSWM_IMMEDIATE")
        .setSourceType("BswMComMIndication")
        .addSourceParameter("BswMComMChannelRef", "/ComM/CAN1")
        .setBswModeInitValue("COMM_NO_COMMUNICATION")
    )
    event_port = BswmEventRequestPort().setName("ERP_1").setRequestProcessing("BSWM_DEFERRED").setSourceType("BswMComMInitiateReset")

    assert condition.getConditionValue("BswMBswRequestedMode") == ["COMM_FULL_COMMUNICATION"]
    assert mode_port.getSourceParameter("BswMComMChannelRef") == ["/ComM/CAN1"]
    assert (mode_port.getBswModeInitValue(), mode_port.getInitCompuConstText(), mode_port.getInitCompuMethodRef()) == ("COMM_NO_COMMUNICATION", None, None)
    assert event_port.getSourceParameters() == {}


def test_bswm_switch_port_general_and_module_collections():
    switch_port = BswmSwitchPort().setName("SP_1").setModeSwitchInterfaceRef("/If/AppMode")
    general = BswmGeneral().setParameter("BswMComMEnabled", True).addUserIncludeFile("App.h")
    module = BswmModule().addRule(BswmRule().setName("R_1")).addLogicalExpression(BswmLogicalExpression().setName("LE_1")).addModeCondition(BswmModeCondition().setName("MC_1"))
    module.addModeRequestPort(BswmModeRequestPort().setName("MRP_1")).addEventRequestPort(BswmEventRequestPort().setName("ERP_1")).addSwitchPort(switch_port).setGeneral(general)

    assert (switch_port.getModeSwitchInterfaceRef(), switch_port.getSchMModeDeclarationGroupRef()) == ("/If/AppMode", None)
    assert general.getParameters() == {"BswMComMEnabled": True}
    assert general.getUserIncludeFiles() == ["App.h"]
    assert [
        len(module.getRules()),
        len(module.getLogicalExpressions()),
        len(module.getModeConditions()),
        len(module.getModeRequestPorts()),
        len(module.getEventRequestPorts()),
        len(module.getSwitchPorts()),
    ] == [1, 1, 1, 1, 1, 1]
    assert module.getGeneral() is general
    assert BswmModule().getGeneral() is None
