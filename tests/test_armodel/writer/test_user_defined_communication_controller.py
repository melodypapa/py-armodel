"""Writer round-trip tests for UserDefinedCommunicationController (Table 3.132, p.180).

XML element order per XSD USER-DEFINED-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd
line 128652): heritage groups (SHORT-NAME via writeIdentifiable) first, then the
own atpVariation group USER-DEFINED-COMMUNICATION-CONTROLLER (lines 128630-128650)
— an optional USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS wrapper whose
USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL carries the inherited
COMMUNICATION-CONTROLLER-CONTENT (WAKE-UP-BY-CONTROLLER-SUPPORTED); the wrapper is
emitted unconditionally per the writeUserDefinedCluster shape.
writeUserDefinedCommunicationController calls the reusable writeCommunicationController
helper exactly once, on the CONDITIONAL; it creates the
USER-DEFINED-COMMUNICATION-CONTROLLER SubElement itself, mirroring the
writeCanCommunicationController shape shared by every writeEcuInstanceCommControllers
branch (the dispatch passes the COMM-CONTROLLERS wrapper element).

Verifies that a UserDefinedCommunicationController created on an EcuInstance survives
a full set -> save -> reload cycle with its inherited CommunicationController
attributes intact, including the bare-controller case.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

COMMUNICATION_CONTROLLER_XSD_ORDER = [
    "SHORT-NAME",
    "USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _reload(parser, path):
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(path, document)
    return document


def _new_controller(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    return UserDefinedCommunicationController(ecu, name)


def _full_controller():
    controller = _new_controller("UserDefinedCommunicationController")
    wakeup_flag = Boolean()
    wakeup_flag.setValue(True)
    controller.setWakeUpByControllerSupported(wakeup_flag)
    return controller


def _write_controller(controller):
    # the COMM-CONTROLLERS dispatch passes the wrapper element; the entry point creates the
    # USER-DEFINED-COMMUNICATION-CONTROLLER SubElement itself (writeCanCommunicationController shape)
    element = ET.Element("COMM-CONTROLLERS")
    ARXMLWriter().writeUserDefinedCommunicationController(element, controller)
    return element[0]


def _namespaced(element):
    xml_text = ET.tostring(element, encoding="unicode")
    return ET.fromstring(xml_text.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))


class TestWriteUserDefinedCommunicationController:
    def test_entry_point_emits_short_name(self):
        element = _write_controller(_full_controller())

        assert element.find("SHORT-NAME").text == "UserDefinedCommunicationController"

    def test_entry_point_writes_inherited_levels_in_xsd_order_exactly_once(self):
        element = _write_controller(_full_controller())

        assert [child.tag for child in element] == COMMUNICATION_CONTROLLER_XSD_ORDER

        # direct children only — the CONDITIONAL legitimately nests its own content under VARIANTS
        for tag in COMMUNICATION_CONTROLLER_XSD_ORDER:
            assert len(element.findall(tag)) == 1, tag

    def test_entry_point_writes_field_values(self):
        element = _write_controller(_full_controller())

        conditional = element.find("USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS/USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert conditional is not None
        assert conditional.find("WAKE-UP-BY-CONTROLLER-SUPPORTED").text == "true"

    def test_bare_controller_emits_wrapper_without_content(self):
        element = _write_controller(_new_controller("Controller"))

        assert element.find("SHORT-NAME").text == "Controller"
        assert [child.tag for child in element] == COMMUNICATION_CONTROLLER_XSD_ORDER
        conditional = element.find("USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS/USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert conditional is not None
        assert conditional.find("WAKE-UP-BY-CONTROLLER-SUPPORTED") is None

    def test_round_trip_full_through_user_defined_communication_controller(self):
        element = _write_controller(_full_controller())
        reloaded = _new_controller("UserDefinedCommunicationController")
        ARXMLParser().readUserDefinedCommunicationController(_namespaced(element), reloaded)

        assert reloaded.getShortName() == "UserDefinedCommunicationController"
        assert reloaded.getWakeUpByControllerSupported().getValue() is True

    def test_round_trip_empty_through_user_defined_communication_controller(self):
        element = _write_controller(_new_controller("Controller"))
        reloaded = _new_controller("Controller")
        ARXMLParser().readUserDefinedCommunicationController(_namespaced(element), reloaded)

        assert reloaded.getShortName() == "Controller"
        assert reloaded.getWakeUpByControllerSupported() is None


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    controller = ecu.createUserDefinedCommunicationController("UserDefinedCommunicationController")
    wakeup_flag = Boolean()
    wakeup_flag.setValue(True)
    controller.setWakeUpByControllerSupported(wakeup_flag)

    out_file = str(tmp_path / "user_defined_communication_controller.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_ecu = re_pkg.getReferrableElement("Ecu", EcuInstance)
    assert re_ecu is not None

    re_controllers = re_ecu.getCommControllers()
    assert len(re_controllers) == 1
    re_controller = re_controllers[0]
    assert isinstance(re_controller, UserDefinedCommunicationController)
    assert re_controller.getShortName() == "UserDefinedCommunicationController"
    assert re_controller.getWakeUpByControllerSupported().getValue() is True


def test_round_trip_empty(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    ecu.createUserDefinedCommunicationController("EmptyController")

    out_file = str(tmp_path / "user_defined_communication_controller_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")

    re_ecu = re_pkg.getReferrableElement("Ecu", EcuInstance)
    re_controllers = re_ecu.getCommControllers()
    assert len(re_controllers) == 1
    assert isinstance(re_controllers[0], UserDefinedCommunicationController)
    assert re_controllers[0].getShortName() == "EmptyController"
    assert re_controllers[0].getWakeUpByControllerSupported() is None
