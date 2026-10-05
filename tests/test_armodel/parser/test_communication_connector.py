"""Parser tests for CommunicationConnector (Table 3.4, p.54).

XML element order per XSD group COMMUNICATION-CONNECTOR: COMM-CONTROLLER-REF,
CREATE-ECU-WAKEUP-SOURCE, DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED,
ECU-COMM-PORT-INSTANCES, PNC-FILTER-ARRAY-MASKS, PNC-GATEWAY-TYPE.
Coverage runs through the CONNECTORS dispatch on readEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FramePort
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CONNECTOR = (
    "<CONNECTORS>"
    "<CAN-COMMUNICATION-CONNECTOR>"
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


class TestReadCommunicationConnector:
    def test_dispatch_creates_connector_with_short_name(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connectors = instance.getConnectors()
        assert len(connectors) == 1
        assert isinstance(connectors[0], CanCommunicationConnector)
        assert connectors[0].getShortName() == "conn"

    def test_reads_comm_controller_ref_with_dest(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]
        ref = connector.getCommControllerRef()
        assert ref is not None
        assert ref.getValue() == "/can/ctrl"
        assert ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"

    def test_reads_boolean_attributes_with_values_and_types(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]

        wakeup = connector.getCreateEcuWakeupSource()
        assert isinstance(wakeup, Boolean)
        assert wakeup.getValue() is True

        mapping = connector.getDynamicPncToChannelMappingEnabled()
        assert isinstance(mapping, Boolean)
        assert mapping.getValue() is False

    def test_reads_frame_port_child_values(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]
        ports = connector.getEcuCommPortInstances()
        assert len(ports) == 1
        assert isinstance(ports[0], FramePort)
        assert ports[0].getShortName() == "fp"
        assert ports[0].getCommunicationDirection().getValue() == "in"

    def test_reads_pnc_filter_array_masks_as_typed_integers_in_document_order(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]
        masks = connector.getPncFilterArrayMasks()
        assert len(masks) == 2
        assert all(isinstance(mask, PositiveInteger) for mask in masks)
        assert [mask.getValue() for mask in masks] == [255, 1]

    def test_reads_pnc_gateway_type_value(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]
        assert connector.getPncGatewayType().getValue() == "active"

    def test_reads_connector_without_optional_elements_to_empty_fields(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connector = instance.getConnectors()[0]
        assert connector.getCommControllerRef() is None
        assert connector.getCreateEcuWakeupSource() is None
        assert connector.getDynamicPncToChannelMappingEnabled() is None
        assert connector.getEcuCommPortInstances() == []
        assert connector.getPncFilterArrayMasks() == []
        assert connector.getPncGatewayType() is None
