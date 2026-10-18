from pathlib import Path

import pytest

from armodel.data_models.ecuc import BswmModule
from armodel.parser import BswmEcucParser

FIXTURE = Path(__file__).parent / "data" / "bswm_ecuc_partitions.arxml"


@pytest.fixture(scope="module")
def module() -> BswmModule:
    return BswmEcucParser().load(str(FIXTURE), warning=False)


def test_every_element_records_its_path_and_partition(module: BswmModule):
    actions = [(action.getName(), action.getPartition(), action.getPath()) for action in module.getActions()]

    assert actions == [
        ("AC_RteModeRequest", "BswMConfig_P0", "/Vendor/BswM/BswMConfig_P0/BswMModeControl/AC_RteModeRequest"),
        ("AC_Start", "BswMConfig_P0", "/Vendor/BswM/BswMConfig_P0/BswMModeControl/AC_Start"),
        ("AC_Start", "BswMConfig_P1", "/Vendor/BswM/BswMConfig_P1/BswMModeControl/AC_Start"),
    ]


def test_same_short_names_in_different_partitions_stay_separate(module: BswmModule):
    lists = [(action_list.getName(), action_list.getPartition(), [item.getActionRef() for item in action_list.getItems()]) for action_list in module.getActionLists()]

    assert lists == [
        ("AL_Startup", "BswMConfig_P0", ["/Vendor/BswM/BswMConfig_P0/BswMModeControl/AC_RteModeRequest"]),
        ("AL_Startup", "BswMConfig_P1", ["/Vendor/BswM/BswMConfig_P1/BswMModeControl/AC_Start"]),
    ]


def test_rte_mode_request_port_reads_instance_and_foreign_references(module: BswmModule):
    [port] = module.getRteModeRequestPorts()

    assert port.getName() == "RMP_Mode"
    assert port.getPartition() == "BswMConfig_P0"
    assert port.getInterfaceRef() == "/Vendor/Ports/AppVdp"
    assert port.getVariableDataPrototypeRef() == "/Vendor/Ports/AppVdp"


def test_rte_mode_request_action_keeps_the_port_reference(module: BswmModule):
    request = module.getActions()[0]

    assert request.getActionType() == "BswMRteModeRequest"
    assert request.getParameter("BswMRteModeRequestPortRef") == ["/Vendor/BswM/BswMConfig_P0/BswMModeControl/RMP_Mode"]
    assert request.getParameter("BswMRequestedModeRef") == ["/Vendor/Modes/AppMode/RUN"]


def test_data_type_mapping_sets_are_collected_per_partition(module: BswmModule):
    sets = [(mapping.getPartition(), mapping.getRefs()) for mapping in module.getDataTypeMappingSets()]

    assert sets == [
        ("BswMConfig_P0", ["/Vendor/DataTypeMappings/SetA", "/Vendor/DataTypeMappings/SetB"]),
        ("BswMConfig_P1", ["/Vendor/DataTypeMappings/SetA"]),
    ]


def test_module_level_general_is_read_without_a_partition(module: BswmModule):
    general = module.getGeneral()

    assert general is not None
    assert general.getParameters() == {"BswMComMEnabled": True}
