"""Parser tests for UserDefinedCommunicationConnector (Table 3.131, p.180).

XML element order per XSD USER-DEFINED-COMMUNICATION-CONNECTOR (AUTOSAR_00052.xsd
line 128622): heritage groups (SHORT-NAME via IDENTIFIABLE) first, then the
inherited COMMUNICATION-CONNECTOR group content in sequenceOffset order
(COMM-CONTROLLER-REF, CREATE-ECU-WAKEUP-SOURCE, DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED,
ECU-COMM-PORT-INSTANCES, PNC-FILTER-ARRAY-MASKS, PNC-GATEWAY-TYPE); the
USER-DEFINED-COMMUNICATION-CONNECTOR own group (lines 128603-128611) is an empty
sequence — no atpVariation wrapper.
readUserDefinedCommunicationConnector calls the reusable readCommunicationConnector
helper exactly once (the TtcanCommunicationConnector leveling).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.CddSupport import UserDefinedCommunicationConnector
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_USER_DEFINED_COMMUNICATION_CONNECTOR = (
    "<USER-DEFINED-COMMUNICATION-CONNECTOR>"
    "<SHORT-NAME>Connector</SHORT-NAME>"
    '<COMM-CONTROLLER-REF DEST="CAN-COMMUNICATION-CONTROLLER">/EcuInst/Ctrl</COMM-CONTROLLER-REF>'
    "<CREATE-ECU-WAKEUP-SOURCE>true</CREATE-ECU-WAKEUP-SOURCE>"
    "<ECU-COMM-PORT-INSTANCES>"
    "<I-SIGNAL-PORT>"
    "<SHORT-NAME>Port</SHORT-NAME>"
    "</I-SIGNAL-PORT>"
    "</ECU-COMM-PORT-INSTANCES>"
    "<PNC-FILTER-ARRAY-MASKS>"
    "<PNC-FILTER-ARRAY-MASK>255</PNC-FILTER-ARRAY-MASK>"
    "</PNC-FILTER-ARRAY-MASKS>"
    "<PNC-GATEWAY-TYPE>ACTIVE</PNC-GATEWAY-TYPE>"
    "</USER-DEFINED-COMMUNICATION-CONNECTOR>"
)

BARE_USER_DEFINED_COMMUNICATION_CONNECTOR = "<USER-DEFINED-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>Connector</SHORT-NAME>" "</USER-DEFINED-COMMUNICATION-CONNECTOR>"


def _new_connector(name):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    ecu = pkg.createEcuInstance("Ecu")
    return UserDefinedCommunicationConnector(ecu, name)


def _read_user_defined_communication_connector(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    connector = _new_connector("Connector")
    ARXMLParser().readUserDefinedCommunicationConnector(root[0], connector)
    return connector


class TestReadUserDefinedCommunicationConnector:
    def test_reads_short_name_and_inherited_levels(self):
        connector = _read_user_defined_communication_connector(FULL_USER_DEFINED_COMMUNICATION_CONNECTOR)

        assert connector.getShortName() == "Connector"
        comm_controller_ref = connector.getCommControllerRef()
        assert comm_controller_ref.getValue() == "/EcuInst/Ctrl"
        assert comm_controller_ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"
        assert connector.getCreateEcuWakeupSource().getValue() is True

    def test_reads_ecu_comm_port_instances(self):
        connector = _read_user_defined_communication_connector(FULL_USER_DEFINED_COMMUNICATION_CONNECTOR)

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "Port"

    def test_reads_pnc_levels(self):
        connector = _read_user_defined_communication_connector(FULL_USER_DEFINED_COMMUNICATION_CONNECTOR)

        masks = connector.getPncFilterArrayMasks()
        assert len(masks) == 1
        assert masks[0].getValue() == 255
        assert connector.getPncGatewayType().getValue() == "ACTIVE"

    def test_reads_bare_connector_to_defaults(self):
        connector = _read_user_defined_communication_connector(BARE_USER_DEFINED_COMMUNICATION_CONNECTOR)

        assert connector.getShortName() == "Connector"
        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None
