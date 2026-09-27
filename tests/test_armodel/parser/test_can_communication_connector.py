"""Parser tests for CanCommunicationConnector (Table 3.23, p.74).

XML element order per XSD group CAN-COMMUNICATION-CONNECTOR: PNC-WAKEUP-CAN-ID,
PNC-WAKEUP-CAN-ID-EXTENDED, PNC-WAKEUP-CAN-ID-MASK, PNC-WAKEUP-DATA-MASK, PNC-WAKEUP-DLC.
Coverage runs through the CONNECTORS dispatch on readEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, PositiveUnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import CanCommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_CONNECTOR = (
    "<CONNECTORS>"
    "<CAN-COMMUNICATION-CONNECTOR>"
    "<SHORT-NAME>conn</SHORT-NAME>"
    "<COMM-CONTROLLER-REF DEST='CAN-COMMUNICATION-CONTROLLER'>/can/ctrl</COMM-CONTROLLER-REF>"
    "<PNC-WAKEUP-CAN-ID>401</PNC-WAKEUP-CAN-ID>"
    "<PNC-WAKEUP-CAN-ID-EXTENDED>true</PNC-WAKEUP-CAN-ID-EXTENDED>"
    "<PNC-WAKEUP-CAN-ID-MASK>255</PNC-WAKEUP-CAN-ID-MASK>"
    "<PNC-WAKEUP-DATA-MASK>65535</PNC-WAKEUP-DATA-MASK>"
    "<PNC-WAKEUP-DLC>8</PNC-WAKEUP-DLC>"
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


class TestReadCanCommunicationConnector:
    def test_dispatch_creates_can_connector_with_short_name_and_dest(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connectors = instance.getConnectors()
        assert len(connectors) == 1
        connector = connectors[0]
        assert isinstance(connector, CanCommunicationConnector)
        assert connector.getShortName() == "conn"

    def test_reads_comm_controller_ref_with_dest(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]
        ref = connector.getCommControllerRef()
        assert ref is not None
        assert ref.getValue() == "/can/ctrl"
        assert ref.getDest() == "CAN-COMMUNICATION-CONTROLLER"

    def test_reads_all_five_pnc_fields_with_values_and_types(self, parser):
        instance = _read_into_instance(FULL_CONNECTOR)
        connector = instance.getConnectors()[0]

        can_id = connector.getPncWakeupCanId()
        assert isinstance(can_id, PositiveInteger)
        assert can_id.getValue() == 401

        extended = connector.getPncWakeupCanIdExtended()
        assert isinstance(extended, Boolean)
        assert extended.getValue() is True

        mask = connector.getPncWakeupCanIdMask()
        assert isinstance(mask, PositiveInteger)
        assert mask.getValue() == 255

        data_mask = connector.getPncWakeupDataMask()
        assert isinstance(data_mask, PositiveUnlimitedInteger)
        assert data_mask.getValue() == 65535

        dlc = connector.getPncWakeupDlc()
        assert isinstance(dlc, PositiveInteger)
        assert dlc.getValue() == 8

    def test_reads_connector_without_pnc_elements_to_none_fields(self, parser):
        instance = _read_into_instance(BARE_CONNECTOR)
        connector = instance.getConnectors()[0]
        assert connector.getPncWakeupCanId() is None
        assert connector.getPncWakeupCanIdExtended() is None
        assert connector.getPncWakeupCanIdMask() is None
        assert connector.getPncWakeupDataMask() is None
        assert connector.getPncWakeupDlc() is None
