from armodel.data_models.ecuc import BswmAction, BswmActionList, BswmActionListItem, BswmModule


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
