"""Writer round-trip tests for TtcanCommunicationController (Table 3.25, p.77).

XML element order per XSD TTCAN-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd
line 127016): heritage groups (SHORT-NAME via writeIdentifiable) first, then the
TTCAN-COMMUNICATION-CONTROLLER group's TTCAN-COMMUNICATION-CONTROLLER-VARIANTS/
TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL wrapper carrying the inherited
COMMUNICATION-CONTROLLER + ABSTRACT-CAN-COMMUNICATION-CONTROLLER content in
sequenceOffset order (WAKE-UP-BY-CONTROLLER-SUPPORTED, CAN-CONTROLLER-ATTRIBUTES)
followed by this class's TTCAN-COMMUNICATION-CONTROLLER-CONTENT (line 127068:
APPL-WATCHDOG-LIMIT, EXPECTED-TX-TRIGGER, EXTERNAL-CLOCK-SYNCHRONISATION,
INITIAL-REF-OFFSET, MASTER, TIME-MASTER-PRIORITY, TIME-TRIGGERED-CAN-LEVEL,
TX-ENABLE-WINDOW-LENGTH). writeTtcanCommunicationController calls the
writeAbstractCanCommunicationController helper exactly once. The class is emitted
as a concrete element of the EcuInstance COMM-CONTROLLERS choice (line 50382,
Rule 0001.7).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanControllerConfigurationRequirements, TtcanCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "WAKE-UP-BY-CONTROLLER-SUPPORTED",
    "CAN-CONTROLLER-ATTRIBUTES",
    "APPL-WATCHDOG-LIMIT",
    "EXPECTED-TX-TRIGGER",
    "EXTERNAL-CLOCK-SYNCHRONISATION",
    "INITIAL-REF-OFFSET",
    "MASTER",
    "TIME-MASTER-PRIORITY",
    "TIME-TRIGGERED-CAN-LEVEL",
    "TX-ENABLE-WINDOW-LENGTH",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parent():
    return ET.Element("PARENT")


def _new_controller(name="TtcanCtl"):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return TtcanCommunicationController(pkg, name)


def _full_controller():
    controller = _new_controller()
    controller.setWakeUpByControllerSupported(Boolean().setValue(True))
    requirements = CanControllerConfigurationRequirements()
    requirements.setMinNumberOfTimeQuantaPerBit(Integer().setValue(4))
    controller.setCanControllerAttributes(requirements)
    controller.setApplWatchdogLimit(Integer().setValue(100))
    controller.setExpectedTxTrigger(Integer().setValue(8))
    controller.setExternalClockSynchronisation(Boolean().setValue(True))
    controller.setInitialRefOffset(Integer().setValue(3))
    controller.setMaster(Boolean().setValue(True))
    controller.setTimeMasterPriority(Integer().setValue(5))
    controller.setTimeTriggeredCanLevel(Integer().setValue(2))
    controller.setTxEnableWindowLength(Integer().setValue(12))
    return controller


def _write_ttcan_controller(controller):
    parent = _parent()
    ARXMLWriter().writeTtcanCommunicationController(parent, controller)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteTtcanCommunicationController:
    def test_entry_point_emits_short_name_and_wrapper(self):
        parent = _write_ttcan_controller(_full_controller())
        ttcan_controller = parent.find("TTCAN-COMMUNICATION-CONTROLLER")

        assert ttcan_controller.find("SHORT-NAME").text == "TtcanCtl"
        assert ttcan_controller.find("TTCAN-COMMUNICATION-CONTROLLER-VARIANTS/TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL") is not None

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        parent = _write_ttcan_controller(_full_controller())
        ttcan_controller = parent.find("TTCAN-COMMUNICATION-CONTROLLER")
        conditional = ttcan_controller.find("TTCAN-COMMUNICATION-CONTROLLER-VARIANTS/TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL")

        assert [child.tag for child in conditional] == XSD_ORDER

        all_tags = [child.tag for child in ttcan_controller.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_ttcan_controller(_full_controller())
        conditional = parent.find("TTCAN-COMMUNICATION-CONTROLLER/TTCAN-COMMUNICATION-CONTROLLER-VARIANTS/TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL")

        assert conditional.find("WAKE-UP-BY-CONTROLLER-SUPPORTED").text == "true"
        assert conditional.find("CAN-CONTROLLER-ATTRIBUTES/CAN-CONTROLLER-CONFIGURATION-REQUIREMENTS/MIN-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "4"

        assert conditional.find("APPL-WATCHDOG-LIMIT").text == "100"
        assert conditional.find("EXPECTED-TX-TRIGGER").text == "8"
        assert conditional.find("EXTERNAL-CLOCK-SYNCHRONISATION").text == "true"
        assert conditional.find("INITIAL-REF-OFFSET").text == "3"
        assert conditional.find("MASTER").text == "true"
        assert conditional.find("TIME-MASTER-PRIORITY").text == "5"
        assert conditional.find("TIME-TRIGGERED-CAN-LEVEL").text == "2"
        assert conditional.find("TX-ENABLE-WINDOW-LENGTH").text == "12"

    def test_bare_controller_emits_short_name_and_empty_wrapper(self):
        parent = _write_ttcan_controller(_new_controller())
        ttcan_controller = parent.find("TTCAN-COMMUNICATION-CONTROLLER")

        assert ttcan_controller.find("SHORT-NAME").text == "TtcanCtl"
        conditional = ttcan_controller.find("TTCAN-COMMUNICATION-CONTROLLER-VARIANTS/TTCAN-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert conditional is not None
        assert len(conditional) == 0

    def test_ecu_instance_consumer_emits_comm_controllers_choice(self):
        ecu = EcuInstance(AUTOSAR.getInstance(), "Ecu")
        ecu.createTtcanCommunicationController("TtcanCtl")
        parent = _parent()
        ARXMLWriter().writeEcuInstanceCommControllers(parent, ecu)

        comm_controllers = parent.find("COMM-CONTROLLERS")
        controller_element = comm_controllers.find("TTCAN-COMMUNICATION-CONTROLLER")
        assert controller_element is not None
        assert controller_element.find("SHORT-NAME").text == "TtcanCtl"

    def test_round_trip_full_through_ttcan_communication_controller(self):
        parent = _write_ttcan_controller(_full_controller())
        reloaded = _new_controller()
        ARXMLParser().readTtcanCommunicationController(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "TtcanCtl"
        assert reloaded.getWakeUpByControllerSupported().getValue() is True
        assert reloaded.getCanControllerAttributes().getMinNumberOfTimeQuantaPerBit().getValue() == 4

        assert reloaded.getApplWatchdogLimit().getValue() == 100
        assert reloaded.getExpectedTxTrigger().getValue() == 8
        assert reloaded.getExternalClockSynchronisation().getValue() is True
        assert reloaded.getInitialRefOffset().getValue() == 3
        assert reloaded.getMaster().getValue() is True
        assert reloaded.getTimeMasterPriority().getValue() == 5
        assert reloaded.getTimeTriggeredCanLevel().getValue() == 2
        assert reloaded.getTxEnableWindowLength().getValue() == 12

    def test_round_trip_empty_through_ttcan_communication_controller(self):
        parent = _write_ttcan_controller(_new_controller())
        reloaded = _new_controller()
        ARXMLParser().readTtcanCommunicationController(_namespaced_first_child(parent), reloaded)

        assert reloaded.getShortName() == "TtcanCtl"
        assert reloaded.getWakeUpByControllerSupported() is None
        assert reloaded.getCanControllerAttributes() is None
        assert reloaded.getApplWatchdogLimit() is None
        assert reloaded.getExpectedTxTrigger() is None
        assert reloaded.getExternalClockSynchronisation() is None
        assert reloaded.getInitialRefOffset() is None
        assert reloaded.getMaster() is None
        assert reloaded.getTimeMasterPriority() is None
        assert reloaded.getTimeTriggeredCanLevel() is None
        assert reloaded.getTxEnableWindowLength() is None
