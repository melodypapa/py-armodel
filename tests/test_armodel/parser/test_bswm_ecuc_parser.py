from pathlib import Path

import pytest

from armodel.data_models.ecuc import BswmModule
from armodel.parser import BswmEcucConversionError, BswmEcucParser
from armodel.parser.bswm_ecuc_parser import BSWM_AVAILABLE_ACTIONS

FIXTURE = Path(__file__).parent / "data" / "bswm_ecuc_minimal.arxml"


def load(warning=True) -> BswmModule:
    return BswmEcucParser().load(str(FIXTURE), warning=warning)


def test_available_actions_table_matches_the_sws():
    assert len(BSWM_AVAILABLE_ACTIONS) == 33
    assert BSWM_AVAILABLE_ACTIONS["BswMPduGroupSwitch"] == ["BswMPduGroupSwitchReinit", "BswMDisabledPduGroupRef", "BswMEnabledPduGroupRef"]
    assert BSWM_AVAILABLE_ACTIONS["BswMRteStop"] == []


def test_module_name_comes_from_the_module_configuration():
    assert load().getName() == "BswM"


def test_actions_are_found_below_nested_config_containers():
    module = load()

    assert [(action.getName(), action.getActionType()) for action in module.getActions()] == [
        ("AC_UserCallout", "BswMUserCallout"),
        ("AC_PduGroupSwitch", "BswMPduGroupSwitch"),
        ("AC_VendorOnly", None),
    ]


def test_action_payload_is_typed_by_definition_and_keeps_repeated_references():
    switch = load().getActions()[1]

    assert switch.getParameter("BswMPduGroupSwitchReinit") == [True]
    assert switch.getParameter("BswMEnabledPduGroupRef") == ["/Vendor/Com/ComConfig/IpduGroup_Tx", "/Vendor/Com/ComConfig/IpduGroup_Rx"]
    assert load().getActions()[0].getParameter("BswMUserCalloutFunction") == ["App_OnStartup()"]


def test_parameters_not_defined_in_the_sws_are_dropped():
    switch = load().getActions()[1]
    vendor_only = load().getActions()[2]

    assert list(switch.getParameters()) == ["BswMPduGroupSwitchReinit", "BswMEnabledPduGroupRef"]
    assert vendor_only.getParameters() == {}


def test_action_list_items_convert_numeric_strings_and_resolve_reference_types():
    action_list = load().getActionLists()[0]

    assert action_list.getName() == "AL_Startup"
    assert action_list.getExecution() == "BSWM_TRIGGER"
    assert action_list.getPriority() == 5
    assert [(item.getName(), item.getIndex(), item.getAbortOnFail(), item.getReportFailRuntimeErrorId(), item.getActionRefType()) for item in action_list.getItems()] == [
        ("AI_PduGroupSwitch", 20, False, None, "BswMAction"),
        ("AI_UserCallout", 10, True, 200, "BswMAction"),
        ("AI_Dangling", 30, None, None, None),
    ]
    assert action_list.getItems()[0].getActionRef() == "/Vendor/BswM/BswMConfig_0/BswMModeControl/AC_PduGroupSwitch"


def test_unresolved_item_reference_warns_in_warning_mode(caplog):
    load(warning=True)

    assert "Unresolved standard reference BswMActionListItemRef -> /Vendor/BswM/BswMConfig_0/BswMModeControl/AC_Missing" in caplog.text


def test_unresolved_item_reference_raises_in_strict_mode():
    with pytest.raises(BswmEcucConversionError, match="AC_Missing"):
        load(warning=False)


def test_module_from_file_delegates_to_the_parser():
    module = BswmModule.from_file(str(FIXTURE), warning=True)

    assert len(module.getActions()) == 3
