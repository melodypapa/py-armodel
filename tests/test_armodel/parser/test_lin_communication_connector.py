"""Parser tests for LinCommunicationConnector (Table 3.43, p.98).

XML element order per XSD group LIN-COMMUNICATION-CONNECTOR: INITIAL-NAD,
LIN-CONFIGURABLE-FRAMES/LIN-CONFIGURABLE-FRAME,
LIN-ORDERED-CONFIGURABLE-FRAMES/LIN-ORDERED-CONFIGURABLE-FRAME,
SCHEDULE-CHANGE-NEXT-TIME-BASE.
Coverage runs through the CONNECTORS dispatch on readEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinConfigurableFrame, LinOrderedConfigurableFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CONNECTOR = (
    "<CONNECTORS>"
    "<LIN-COMMUNICATION-CONNECTOR>"
    "<SHORT-NAME>conn</SHORT-NAME>"
    "<COMM-CONTROLLER-REF DEST='LIN-COMMUNICATION-CONTROLLER'>/lin/ctrl</COMM-CONTROLLER-REF>"
    "<INITIAL-NAD>5</INITIAL-NAD>"
    "<LIN-CONFIGURABLE-FRAMES>"
    "<LIN-CONFIGURABLE-FRAME><SHORT-NAME>cfg1</SHORT-NAME><FRAME-REF DEST='LIN-UNCONDITIONAL-FRAME'>/lin/frame1</FRAME-REF><MESSAGE-ID>33</MESSAGE-ID></LIN-CONFIGURABLE-FRAME>"
    "<LIN-CONFIGURABLE-FRAME><SHORT-NAME>cfg2</SHORT-NAME><FRAME-REF DEST='LIN-UNCONDITIONAL-FRAME'>/lin/frame2</FRAME-REF><MESSAGE-ID>34</MESSAGE-ID></LIN-CONFIGURABLE-FRAME>"
    "</LIN-CONFIGURABLE-FRAMES>"
    "<LIN-ORDERED-CONFIGURABLE-FRAMES>"
    "<LIN-ORDERED-CONFIGURABLE-FRAME><SHORT-NAME>ord1</SHORT-NAME><FRAME-REF DEST='LIN-UNCONDITIONAL-FRAME'>/lin/frame1</FRAME-REF><INDEX>3</INDEX></LIN-ORDERED-CONFIGURABLE-FRAME>"
    "</LIN-ORDERED-CONFIGURABLE-FRAMES>"
    "<SCHEDULE-CHANGE-NEXT-TIME-BASE>true</SCHEDULE-CHANGE-NEXT-TIME-BASE>"
    "</LIN-COMMUNICATION-CONNECTOR>"
    "</CONNECTORS>"
)

EMPTY_WRAPPER_CONNECTOR = (
    "<CONNECTORS>" "<LIN-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "<LIN-CONFIGURABLE-FRAMES/>" "<LIN-ORDERED-CONFIGURABLE-FRAMES/>" "</LIN-COMMUNICATION-CONNECTOR>" "</CONNECTORS>"
)

BARE_CONNECTOR = "<CONNECTORS>" "<LIN-COMMUNICATION-CONNECTOR>" "<SHORT-NAME>conn</SHORT-NAME>" "</LIN-COMMUNICATION-CONNECTOR>" "</CONNECTORS>"


def _read_into_instance(inner):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    ARXMLParser().readEcuInstanceConnectors(root, instance)
    return instance


class TestReadLinCommunicationConnector:
    def test_dispatch_creates_lin_connector_with_short_name(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connectors = instance.getConnectors()
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, LinCommunicationConnector)
        assert connector.getShortName() == "conn"

    def test_reads_all_fields_with_values_and_types(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]

        initial_nad = connector.getInitialNad()
        assert isinstance(initial_nad, Integer)
        assert initial_nad.getValue() == 5

        ref = connector.getCommControllerRef()
        assert ref is not None
        assert ref.getValue() == "/lin/ctrl"
        assert ref.getDest() == "LIN-COMMUNICATION-CONTROLLER"

        frames = connector.getLinConfigurableFrames()
        assert len(frames) == 2
        assert all(isinstance(frame, LinConfigurableFrame) for frame in frames)
        assert frames[0].getFrameRef().getValue() == "/lin/frame1"
        assert frames[0].getFrameRef().getDest() == "LIN-UNCONDITIONAL-FRAME"
        assert frames[0].getMessageId().getValue() == 33
        assert frames[1].getFrameRef().getValue() == "/lin/frame2"
        assert frames[1].getMessageId().getValue() == 34

        ordered_frames = connector.getLinOrderedConfigurableFrames()
        assert len(ordered_frames) == 1
        assert isinstance(ordered_frames[0], LinOrderedConfigurableFrame)
        assert ordered_frames[0].getFrameRef().getValue() == "/lin/frame1"
        assert ordered_frames[0].getIndex().getValue() == 3

        flag = connector.getScheduleChangeNextTimeBase()
        assert isinstance(flag, Boolean)
        assert flag.getValue() is True

    def test_reads_empty_wrappers_to_empty_lists(self, parser):
        instance = _read_into_instance(EMPTY_WRAPPER_CONNECTOR)
        connector = instance.getConnectors()[0]
        assert connector.getLinConfigurableFrames() == []
        assert connector.getLinOrderedConfigurableFrames() == []
        assert connector.getInitialNad() is None
        assert connector.getScheduleChangeNextTimeBase() is None

    def test_reads_connector_without_lin_elements_to_none_fields(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connector = instance.getConnectors()[0]
        assert connector.getInitialNad() is None
        assert connector.getLinConfigurableFrames() == []
        assert connector.getLinOrderedConfigurableFrames() == []
        assert connector.getScheduleChangeNextTimeBase() is None
