"""Parser tests for FlexrayCommunicationConnector (Table 3.33, p.89).

XML element order per XSD group FLEXRAY-COMMUNICATION-CONNECTOR: NM-READY-SLEEP-TIME,
WAKE-UP-CHANNEL (PNC-FILTER-DATA-MASK carries atp.Status="removed" in R23-11 and is
not serialized). Coverage runs through the CONNECTORS dispatch on readEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CONNECTOR = (
    "<CONNECTORS>"
    "<FLEXRAY-COMMUNICATION-CONNECTOR>"
    "<SHORT-NAME>conn</SHORT-NAME>"
    "<COMM-CONTROLLER-REF DEST='FLEXRAY-COMMUNICATION-CONTROLLER'>/flexray/ctrl</COMM-CONTROLLER-REF>"
    "<NM-READY-SLEEP-TIME>10.5</NM-READY-SLEEP-TIME>"
    "<WAKE-UP-CHANNEL>true</WAKE-UP-CHANNEL>"
    "</FLEXRAY-COMMUNICATION-CONNECTOR>"
    "</CONNECTORS>"
)

BARE_CONNECTOR = "<CONNECTORS>" "<FLEXRAY-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</FLEXRAY-COMMUNICATION-CONNECTOR>" "</CONNECTORS>"


def _read_into_instance(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceConnectors(root, instance)
    return instance


class TestReadFlexrayCommunicationConnector:
    def test_dispatch_creates_flexray_connector_with_short_name(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connectors = instance.getConnectors()
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, FlexrayCommunicationConnector)
        assert connector.getShortName() == "conn"

    def test_reads_all_fields_with_values_and_types(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]

        ref = connector.getCommControllerRef()
        assert ref is not None
        assert ref.getValue() == "/flexray/ctrl"
        assert ref.getDest() == "FLEXRAY-COMMUNICATION-CONTROLLER"

        seconds = connector.getNmReadySleepTime()
        assert isinstance(seconds, Float)
        assert seconds.getValue() == 10.5

        flag = connector.getWakeUpChannel()
        assert isinstance(flag, Boolean)
        assert flag.getValue() is True

    def test_reads_connector_without_flexray_elements_to_none_fields(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connector = instance.getConnectors()[0]
        assert connector.getNmReadySleepTime() is None
        assert connector.getWakeUpChannel() is None
