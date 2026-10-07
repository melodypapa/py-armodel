"""Parser tests for UserDefinedCommunicationController (Table 3.132, p.180).

XML element order per XSD USER-DEFINED-COMMUNICATION-CONTROLLER (AUTOSAR_00052.xsd
line 128652): heritage groups (SHORT-NAME via IDENTIFIABLE) first, then the own
atpVariation group USER-DEFINED-COMMUNICATION-CONTROLLER (lines 128630-128650) —
an optional USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS wrapper whose
USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL carries the inherited
COMMUNICATION-CONTROLLER-CONTENT (WAKE-UP-BY-CONTROLLER-SUPPORTED).
readUserDefinedCommunicationController calls readIdentifiable at its own level and
the reusable readCommunicationController helper exactly once, on the CONDITIONAL
(the readUserDefinedCluster leveling).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCommunicationController
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_USER_DEFINED_COMMUNICATION_CONTROLLER = (
    "<USER-DEFINED-COMMUNICATION-CONTROLLER>"
    "<SHORT-NAME>Controller</SHORT-NAME>"
    "<USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS>"
    "<USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "<WAKE-UP-BY-CONTROLLER-SUPPORTED>true</WAKE-UP-BY-CONTROLLER-SUPPORTED>"
    "</USER-DEFINED-COMMUNICATION-CONTROLLER-CONDITIONAL>"
    "</USER-DEFINED-COMMUNICATION-CONTROLLER-VARIANTS>"
    "</USER-DEFINED-COMMUNICATION-CONTROLLER>"
)

BARE_USER_DEFINED_COMMUNICATION_CONTROLLER = "<USER-DEFINED-COMMUNICATION-CONTROLLER>" "<SHORT-NAME>Controller</SHORT-NAME>" "</USER-DEFINED-COMMUNICATION-CONTROLLER>"


def _new_controller(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    return UserDefinedCommunicationController(ecu, name)


def _read_user_defined_communication_controller(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    controller = _new_controller("Controller")
    ARXMLParser().readUserDefinedCommunicationController(root[0], controller)
    return controller


class TestReadUserDefinedCommunicationController:
    def test_reads_short_name_and_inherited_levels(self):
        controller = _read_user_defined_communication_controller(FULL_USER_DEFINED_COMMUNICATION_CONTROLLER)

        assert controller.getShortName() == "Controller"
        assert controller.getWakeUpByControllerSupported().getValue() is True

    def test_reads_bare_controller_to_defaults(self):
        controller = _read_user_defined_communication_controller(BARE_USER_DEFINED_COMMUNICATION_CONTROLLER)

        assert controller.getShortName() == "Controller"
        assert controller.getWakeUpByControllerSupported() is None
