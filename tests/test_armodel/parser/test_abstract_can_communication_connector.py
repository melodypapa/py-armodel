"""Parser tests for AbstractCanCommunicationConnector (Table 3.22, p.73).

The class is abstract with no own attribute rows (Table 3.22 renders the
Attribute header only) and its XSD group ABSTRACT-CAN-COMMUNICATION-CONNECTOR
(AUTOSAR_00052.xsd line 135) is an empty <xsd:sequence/>: the abstract level
contributes no XML elements of its own. Coverage therefore runs through the
concrete CAN-COMMUNICATION-CONNECTOR path (the CONNECTORS dispatch on
readEcuInstanceConnectors, whose readCanCommunicationConnector entry helper
calls the base readCommunicationConnector helper exactly once) and asserts the
instance read is an AbstractCanCommunicationConnector whose inherited
CommunicationConnector fields carry the parsed values.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import AbstractCanCommunicationConnector, CanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CONNECTOR = (
    "<CONNECTORS>"
    "<CAN-COMMUNICATION-CONNECTOR UUID='test-uuid-322'>"
    "<SHORT-NAME>conn</SHORT-NAME>"
    "<COMM-CONTROLLER-REF DEST='CAN-COMMUNICATION-CONTROLLER'>/can/ctrl</COMM-CONTROLLER-REF>"
    "<CREATE-ECU-WAKEUP-SOURCE>true</CREATE-ECU-WAKEUP-SOURCE>"
    "<DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED>false</DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED>"
    "<ECU-COMM-PORT-INSTANCES>"
    "<FRAME-PORT>"
    "<SHORT-NAME>fp</SHORT-NAME>"
    "<COMMUNICATION-DIRECTION>in</COMMUNICATION-DIRECTION>"
    "</FRAME-PORT>"
    "</ECU-COMM-PORT-INSTANCES>"
    "<PNC-FILTER-ARRAY-MASKS>"
    "<PNC-FILTER-ARRAY-MASK>255</PNC-FILTER-ARRAY-MASK>"
    "<PNC-FILTER-ARRAY-MASK>1</PNC-FILTER-ARRAY-MASK>"
    "</PNC-FILTER-ARRAY-MASKS>"
    "<PNC-GATEWAY-TYPE>active</PNC-GATEWAY-TYPE>"
    "<PNC-WAKEUP-CAN-ID>401</PNC-WAKEUP-CAN-ID>"
    "</CAN-COMMUNICATION-CONNECTOR>"
    "</CONNECTORS>"
)

BARE_CONNECTOR = "<CONNECTORS>" "<CAN-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</CAN-COMMUNICATION-CONNECTOR>" "</CONNECTORS>"


def _read_into_instance(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceConnectors(root, instance)
    return instance


class TestReadAbstractCanCommunicationConnector:
    def test_reads_instance_of_abstract_can_communication_connector(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connectors = instance.getConnectors()
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, AbstractCanCommunicationConnector)
        assert isinstance(connector, CanCommunicationConnector)
        assert connector.getShortName() == "conn"

    def test_reads_inherited_fields_with_values(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]

        assert connector.getUuid().getValue() == "test-uuid-322"

        ref = connector.getCommControllerRef()
        assert ref is not None
        assert ref.getValue() == "/can/ctrl"
        assert ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"

        assert connector.getCreateEcuWakeupSource().getValue() is True
        assert connector.getDynamicPncToChannelMappingEnabled().getValue() is False

        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "in"

        masks = connector.getPncFilterArrayMasks()
        assert [mask.getValue() for mask in masks] == [255, 1]

        assert connector.getPncGatewayType().getValue() == "active"

    def test_empty_connector_leaves_inherited_fields_default(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connector = instance.getConnectors()[0]

        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None
