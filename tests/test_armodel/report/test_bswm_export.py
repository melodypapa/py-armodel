from pathlib import Path

import pytest
import yaml
from openpyxl import load_workbook

from armodel.data_models.ecuc import BswmAction, BswmActionList, BswmActionListItem, BswmModule
from armodel.report import BswmConfigExporter, BswmConfigModelMapper, BswmConfigXlsxExporter


def build_module() -> BswmModule:
    module = BswmModule().setName("BswM")
    module.addAction(BswmAction().setName("AC_UserCallout").setActionType("BswMUserCallout").addParameter("BswMUserCalloutFunction", "App_OnStartup()"))
    module.addAction(
        BswmAction()
        .setName("AC_PduGroupSwitch")
        .setActionType("BswMPduGroupSwitch")
        .addParameter("BswMPduGroupSwitchReinit", True)
        .addParameter("BswMEnabledPduGroupRef", "/Com/Tx")
        .addParameter("BswMEnabledPduGroupRef", "/Com/Rx")
    )
    action_list = BswmActionList().setName("AL_Startup").setExecution("BSWM_TRIGGER").setPriority(5)
    action_list.addItem(BswmActionListItem().setName("AI_Second").setIndex(20).setAbortOnFail(False).setActionRef("/BswM/C/AC_PduGroupSwitch").setActionRefType("BswMAction"))
    action_list.addItem(
        BswmActionListItem().setName("AI_First").setIndex(10).setAbortOnFail(True).setReportFailRuntimeErrorId(200).setActionRef("/BswM/C/AC_UserCallout").setActionRefType("BswMAction")
    )
    module.addActionList(action_list)
    module.addActionList(BswmActionList().setName("AL_Empty").setExecution("BSWM_CONDITION"))
    return module


def test_mapper_flattens_actions_with_one_column_per_parameter():
    rows = BswmConfigModelMapper().to_dict(build_module())["BswMAction"]

    assert rows[0] == {"name": "AC_UserCallout", "BswMActionType": "BswMUserCallout", "UsedByActionLists": ["AL_Startup"], "BswMUserCalloutFunction": "App_OnStartup()"}
    assert rows[1]["BswMEnabledPduGroupRef"] == ["/Com/Tx", "/Com/Rx"]
    assert rows[1]["BswMPduGroupSwitchReinit"] is True


def test_mapper_writes_one_action_list_row_per_item_sorted_by_index():
    rows = BswmConfigModelMapper().to_dict(build_module())["BswMActionList"]

    assert [(row["name"], row["BswMActionListItem"], row["BswMActionListItemIndex"], row["BswMActionListItemRef"]) for row in rows] == [
        ("AL_Startup", "AI_First", 10, "AC_UserCallout"),
        ("AL_Startup", "AI_Second", 20, "AC_PduGroupSwitch"),
        ("AL_Empty", None, None, None),
    ]


def test_xlsx_has_action_sheets_first_with_union_headers(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(build_module(), output)

    workbook = load_workbook(output)
    assert workbook.sheetnames[:2] == ["BswMAction", "BswMActionList"]
    action_sheet = workbook["BswMAction"]
    assert [cell.value for cell in action_sheet[1]] == ["name", "BswMActionType", "UsedByActionLists", "BswMUserCalloutFunction", "BswMPduGroupSwitchReinit", "BswMEnabledPduGroupRef"]
    assert action_sheet.cell(row=3, column=6).value == "/Com/Tx\n/Com/Rx"
    list_sheet = workbook["BswMActionList"]
    assert [cell.value for cell in list_sheet[1]] == [
        "name",
        "BswMActionListExecution",
        "BswMActionListPriority",
        "BswMActionListItem",
        "BswMActionListItemIndex",
        "BswMAbortOnFail",
        "BswMReportFailRuntimeErrorId",
        "BswMActionListItemRef",
        "BswMActionListItemRefType",
        "UsedByRules",
        "UsedByActionLists",
    ]
    assert (list_sheet.cell(row=2, column=3).value, list_sheet.cell(row=2, column=4).value, list_sheet.cell(row=2, column=7).value) == (5, "AI_First", 200)


def test_xlsx_writes_headers_for_an_empty_module(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(BswmModule().setName("BswM"), output)

    workbook = load_workbook(output)
    assert [cell.value for cell in workbook["BswMAction"][1]] == ["name", "BswMActionType", "UsedByActionLists"]


def test_yaml_export_omits_empty_values(tmp_path: Path):
    output = tmp_path / "bswm.yaml"

    BswmConfigExporter().export(build_module(), output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert data["BswMAction"][0] == {"name": "AC_UserCallout", "BswMActionType": "BswMUserCallout", "UsedByActionLists": ["AL_Startup"], "BswMUserCalloutFunction": "App_OnStartup()"}
    assert data["BswMActionList"][2] == {"name": "AL_Empty", "BswMActionListExecution": "BSWM_CONDITION"}


def test_exporter_rejects_unsupported_extension(tmp_path: Path):
    with pytest.raises(ValueError, match="Unsupported BswM configuration export format: json"):
        BswmConfigExporter().export(build_module(), tmp_path / "bswm.json")


from armodel.parser import BswmEcucParser  # noqa: E402

ARBITRATION_FIXTURE = Path(__file__).resolve().parents[1] / "parser" / "data" / "bswm_ecuc_arbitration.arxml"

ALL_SHEETS = ["BswMAction", "BswMActionList", "BswMRule", "BswMLogicalExpression", "BswMModeCondition", "BswMModeRequestPort", "BswMEventRequestPort", "BswMSwitchPort", "BswMGeneral", "BswMChecks"]


def arbitration_sections():
    return BswmConfigModelMapper().to_dict(BswmEcucParser().load(str(ARBITRATION_FIXTURE), warning=False))


def test_sections_follow_the_sws_decision_chain():
    assert list(arbitration_sections()) == ALL_SHEETS


def test_rule_expression_and_condition_rows_use_short_names_and_used_by():
    data = arbitration_sections()

    assert data["BswMRule"] == [
        {
            "name": "R_CAN1",
            "BswMRuleInitState": "BSWM_UNDEFINED",
            "BswMNestedExecutionOnly": False,
            "BswMRuleExpressionRef": "LE_Outer",
            "BswMRuleTrueActionList": "AL_Startup",
            "BswMRuleFalseActionList": None,
            "UsedByActionLists": ["AL_Startup"],
        }
    ]
    expressions = {row["name"]: row for row in data["BswMLogicalExpression"]}
    assert expressions["LE_CAN1"]["BswMArgumentRef"] == ["MC_CAN1_FULL", "MC_Reset"]
    assert expressions["LE_CAN1"]["UsedByExpressions"] == ["LE_Outer"]
    assert expressions["LE_Outer"]["UsedByRules"] == ["R_CAN1"]
    conditions = {row["name"]: row for row in data["BswMModeCondition"]}
    assert (conditions["MC_CAN1_FULL"]["BswMConditionMode"], conditions["MC_CAN1_FULL"]["BswMConditionValue"], conditions["MC_CAN1_FULL"]["UsedByExpressions"]) == (
        "MRP_ComM_CAN1",
        "COMM_FULL_COMMUNICATION",
        ["LE_CAN1"],
    )


def test_port_switch_port_and_general_rows():
    data = arbitration_sections()

    [mode_port] = data["BswMModeRequestPort"]
    assert (mode_port["BswMModeRequestSourceType"], mode_port["BswMComMChannelRef"], mode_port["BswMBswModeInitValue"], mode_port["UsedByConditions"]) == (
        "BswMComMIndication",
        "/Vendor/ComM/ComMConfigSet/CAN1",
        "COMM_NO_COMMUNICATION",
        ["MC_CAN1_FULL"],
    )
    assert data["BswMEventRequestPort"][0]["UsedByConditions"] == ["MC_Reset"]
    assert data["BswMSwitchPort"][0]["UsedByActions"] == ["AC_RteSwitch"]
    assert data["BswMGeneral"] == [{"BswMComMEnabled": True, "BswMMainFunctionPeriod": 0.01, "BswMUserIncludeFile": ["App.h", "Diag.h"]}]
    assert data["BswMActionList"][0]["UsedByRules"] == ["R_CAN1"]


def test_xlsx_writes_all_sheets_in_order(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(BswmEcucParser().load(str(ARBITRATION_FIXTURE), warning=False), output)

    assert load_workbook(output).sheetnames == ALL_SHEETS
