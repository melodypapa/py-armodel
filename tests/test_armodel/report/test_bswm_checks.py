from pathlib import Path

from armodel.data_models.ecuc import BswmAction, BswmActionList, BswmActionListItem, BswmModule, BswmRule
from armodel.parser import BswmEcucParser
from armodel.report import BswmConfigChecker, BswmConfigModelMapper

FIXTURE = Path(__file__).resolve().parents[1] / "parser" / "data" / "bswm_ecuc_arbitration.arxml"


def fixture_checks():
    return BswmConfigChecker().check(BswmEcucParser().load(str(FIXTURE), warning=False))


def test_fixture_violations_are_reported_in_check_order():
    assert [(row["Rule"], row["Element"]) for row in fixture_checks()] == [
        ("SWS_BswM_00243", "LE_CAN1"),
        ("SWS_BswM_00256", "MC_Reset"),
        ("SWS_BswM_CONSTR_00001", "AL_Startup"),
        ("SWS_BswM_00240", "AI_Switch"),
        ("SWS_BswM_00037", "AL_Startup"),
    ]


def test_messages_explain_the_violation():
    messages = {row["Rule"]: row["Message"] for row in fixture_checks()}

    assert "exactly 1 argument" in messages["SWS_BswM_00243"]
    assert "BswMEventRequestPort" in messages["SWS_BswM_00256"]
    assert "AI_Switch" in messages["SWS_BswM_CONSTR_00001"] and "AI_Nested" in messages["SWS_BswM_CONSTR_00001"]
    assert "300" in messages["SWS_BswM_00240"]
    assert "cyclic" in messages["SWS_BswM_00037"]


def test_same_group_enabled_and_disabled_is_reported():
    module = BswmModule().addAction(
        BswmAction().setName("AC_1").setActionType("BswMPduGroupSwitch").addParameter("BswMEnabledPduGroupRef", "/Com/G1").addParameter("BswMDisabledPduGroupRef", "/Com/G1")
    )

    assert [(row["Rule"], row["Element"]) for row in BswmConfigChecker().check(module)] == [("SWS_BswM_CONSTR_00004", "AC_1")]


def test_nesting_deeper_than_seven_levels_is_reported():
    module = BswmModule()
    for level in range(9):
        action_list = BswmActionList().setName("AL_%d" % level)
        if level < 8:
            action_list.addItem(BswmActionListItem().setName("AI_%d" % level).setIndex(0).setActionRef("/B/AL_%d" % (level + 1)).setActionRefType("BswMActionList"))
        module.addActionList(action_list)
    module.addRule(BswmRule().setName("R_unused"))

    rows = BswmConfigChecker().check(module)

    assert [(row["Rule"], row["Element"]) for row in rows] == [("SWS_BswM_00037", "AL_0"), ("SWS_BswM_00037", "AL_1")]


def test_mapper_writes_the_checks_section():
    module = BswmEcucParser().load(str(FIXTURE), warning=False)

    assert len(BswmConfigModelMapper().to_dict(module)["BswMChecks"]) == 5
