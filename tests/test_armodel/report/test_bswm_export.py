from pathlib import Path

import pytest
import yaml
from openpyxl import load_workbook

from armodel.data_models.ecuc import BswmAction, BswmActionList, BswmActionListItem, BswmModule
from armodel.parser import BswmEcucParser
from armodel.report import BswmConfigExporter, BswmConfigModelMapper, BswmConfigXlsxExporter

ARBITRATION_FIXTURE = Path(__file__).resolve().parents[1] / "parser" / "data" / "bswm_ecuc_arbitration.arxml"
PARTITION_FIXTURE = Path(__file__).resolve().parents[1] / "parser" / "data" / "bswm_ecuc_partitions.arxml"

ALL_SHEETS = [
    "BswMAction",
    "BswMActionList",
    "BswMRule",
    "BswMLogicalExpression",
    "BswMModeCondition",
    "BswMModeRequestPort",
    "BswMEventRequestPort",
    "BswMSwitchPort",
    "BswMRteModeRequestPort",
    "BswMDataTypeMappingSets",
    "BswMGeneral",
    "BswMChecks",
]


def build_module() -> BswmModule:
    module = BswmModule().setName("BswM")
    module.addAction(BswmAction().setName("AC_UserCallout").setPath("/BswM/C/AC_UserCallout").setActionType("BswMUserCallout").addParameter("BswMUserCalloutFunction", "App_OnStartup()"))
    module.addAction(
        BswmAction()
        .setName("AC_PduGroupSwitch")
        .setPath("/BswM/C/AC_PduGroupSwitch")
        .setActionType("BswMPduGroupSwitch")
        .addParameter("BswMPduGroupSwitchReinit", True)
        .addParameter("BswMEnabledPduGroupRef", "/Com/Tx")
        .addParameter("BswMEnabledPduGroupRef", "/Com/Rx")
    )
    action_list = BswmActionList().setName("AL_Startup").setPath("/BswM/C/AL_Startup").setExecution("BSWM_TRIGGER").setPriority(5)
    action_list.addItem(BswmActionListItem().setName("AI_Second").setIndex(20).setAbortOnFail(False).setActionRef("/BswM/C/AC_PduGroupSwitch").setActionRefType("BswMAction"))
    action_list.addItem(
        BswmActionListItem().setName("AI_First").setIndex(10).setAbortOnFail(True).setReportFailRuntimeErrorId(200).setActionRef("/BswM/C/AC_UserCallout").setActionRefType("BswMAction")
    )
    module.addActionList(action_list)
    module.addActionList(BswmActionList().setName("AL_Empty").setPath("/BswM/C/AL_Empty").setExecution("BSWM_CONDITION"))
    return module


def test_mapper_flattens_actions_with_one_column_per_parameter():
    rows = BswmConfigModelMapper().to_dict(build_module())["BswMAction"]

    assert rows[0] == {"name": "AC_UserCallout", "BswMConfig": None, "BswMActionType": "BswMUserCallout", "UsedByActionLists": ["AL_Startup"], "BswMUserCalloutFunction": "App_OnStartup()"}
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
    assert [cell.value for cell in action_sheet[1]] == ["name", "BswMConfig", "BswMActionType", "UsedByActionLists", "BswMUserCalloutFunction", "BswMPduGroupSwitchReinit", "BswMEnabledPduGroupRef"]
    assert action_sheet.cell(row=3, column=7).value == "/Com/Tx\n/Com/Rx"
    list_sheet = workbook["BswMActionList"]
    assert [cell.value for cell in list_sheet[1]] == [
        "name",
        "BswMConfig",
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
    assert (list_sheet.cell(row=2, column=4).value, list_sheet.cell(row=2, column=5).value, list_sheet.cell(row=2, column=8).value) == (5, "AI_First", 200)


def test_xlsx_writes_headers_for_an_empty_module(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(BswmModule().setName("BswM"), output)

    workbook = load_workbook(output)
    assert [cell.value for cell in workbook["BswMAction"][1]] == ["name", "BswMConfig", "BswMActionType", "UsedByActionLists"]


def test_yaml_export_omits_empty_values(tmp_path: Path):
    output = tmp_path / "bswm.yaml"

    BswmConfigExporter().export(build_module(), output)

    data = yaml.safe_load(output.read_text(encoding="utf-8"))
    assert data["BswMAction"][0] == {"name": "AC_UserCallout", "BswMActionType": "BswMUserCallout", "UsedByActionLists": ["AL_Startup"], "BswMUserCalloutFunction": "App_OnStartup()"}
    assert data["BswMActionList"][2] == {"name": "AL_Empty", "BswMActionListExecution": "BSWM_CONDITION"}


def test_exporter_rejects_unsupported_extension(tmp_path: Path):
    with pytest.raises(ValueError, match="Unsupported BswM configuration export format: json"):
        BswmConfigExporter().export(build_module(), tmp_path / "bswm.json")


def arbitration_sections():
    return BswmConfigModelMapper().to_dict(BswmEcucParser().load(str(ARBITRATION_FIXTURE), warning=False))


def test_sections_follow_the_sws_decision_chain():
    assert list(arbitration_sections()) == ALL_SHEETS


def test_rule_expression_and_condition_rows_use_short_names_and_used_by():
    data = arbitration_sections()

    assert data["BswMRule"] == [
        {
            "name": "R_CAN1",
            "BswMConfig": "BswMConfig_0",
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


def partition_sections():
    return BswmConfigModelMapper().to_dict(BswmEcucParser().load(str(PARTITION_FIXTURE), warning=False))


def test_partition_column_names_the_owning_bswmconfig():
    data = partition_sections()

    assert [(row["name"], row["BswMConfig"]) for row in data["BswMAction"]] == [("AC_RteModeRequest", "BswMConfig_P0"), ("AC_Start", "BswMConfig_P0"), ("AC_Start", "BswMConfig_P1")]


def test_used_by_follows_the_element_path_not_the_short_name():
    actions = partition_sections()["BswMAction"]

    p0_start, p1_start = actions[1], actions[2]
    assert (p0_start["BswMConfig"], p0_start["UsedByActionLists"]) == ("BswMConfig_P0", [])
    assert (p1_start["BswMConfig"], p1_start["UsedByActionLists"]) == ("BswMConfig_P1", ["AL_Startup"])


def test_rte_mode_request_port_and_its_users():
    [port] = partition_sections()["BswMRteModeRequestPort"]

    assert port == {
        "name": "RMP_Mode",
        "BswMConfig": "BswMConfig_P0",
        "BswMRteModeRequestPortInterfaceRef": "AppVdp",
        "BswMRteModeRequestVariableDataPrototypeSRRef": "AppVdp",
        "UsedByActions": ["AC_RteModeRequest"],
    }


def test_data_type_mapping_sets_have_one_row_per_reference():
    rows = partition_sections()["BswMDataTypeMappingSets"]

    assert rows == [
        {"BswMConfig": "BswMConfig_P0", "BswMDataTypeMappingSetRef": "SetA"},
        {"BswMConfig": "BswMConfig_P0", "BswMDataTypeMappingSetRef": "SetB"},
        {"BswMConfig": "BswMConfig_P1", "BswMDataTypeMappingSetRef": "SetA"},
    ]


def test_partition_workbook_has_the_new_sheets_and_headers(tmp_path: Path):
    output = tmp_path / "bswm.xlsx"

    BswmConfigXlsxExporter().export(BswmEcucParser().load(str(PARTITION_FIXTURE), warning=False), output)

    workbook = load_workbook(output)
    assert workbook["BswMRteModeRequestPort"][2][0].value == "RMP_Mode"
    assert [cell.value for cell in workbook["BswMDataTypeMappingSets"][1]] == ["BswMConfig", "BswMDataTypeMappingSetRef"]
