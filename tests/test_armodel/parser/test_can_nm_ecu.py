"""Parser tests for CanNmEcu (Table 6.312, p.683).

R23-11 table has zero attribute rows; the XSD group CAN-NM-ECU's only element
(NM-REPEAT-MSG-INDICATION-ENABLED) carries atp.Status="removed" and is not
modeled. Coverage runs through the BUS-DEPENDENT-NM-ECUS wrapper dispatch on
NmEcu; the S/T ARObject level (Rule 0025) round-trips through readCanNmEcu.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import CanNmEcu, NmEcu
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _parse_ecus(xml):
    root = ET.fromstring(xml)
    nm_ecu = NmEcu(MockParent(), "NmEcu1")
    ARXMLParser().readBusDependentNmEcus(root, nm_ecu)
    return nm_ecu.getBusDependentNmEcus()


class TestParseCanNmEcu:
    def test_parse_dispatch(self):
        xml = "<NM-ECU xmlns='%s'><SHORT-NAME>NmEcu1</SHORT-NAME><BUS-DEPENDENT-NM-ECUS><CAN-NM-ECU/></BUS-DEPENDENT-NM-ECUS></NM-ECU>" % NS
        dependent = _parse_ecus(xml)
        assert len(dependent) == 1
        assert isinstance(dependent[0], CanNmEcu)

    def test_parse_base_s_t_attributes(self):
        xml = (
            "<NM-ECU xmlns='%(ns)s'>"
            "<SHORT-NAME>NmEcu1</SHORT-NAME>"
            "<BUS-DEPENDENT-NM-ECUS>"
            '<CAN-NM-ECU S="42" T="2023-01-01T00:00:00+02:00"/>'
            "</BUS-DEPENDENT-NM-ECUS>"
            "</NM-ECU>" % {"ns": NS}
        )
        dependent = _parse_ecus(xml)
        ecu = dependent[0]
        assert ecu.getChecksum() is not None
        assert ecu.getChecksum().getValue() == "42"
        assert ecu.getTimestamp() is not None
        assert ecu.getTimestamp().getValue() == "2023-01-01T00:00:00+02:00"

    def test_parse_empty_ecu_has_no_base_attributes(self):
        xml = "<NM-ECU xmlns='%s'><SHORT-NAME>NmEcu1</SHORT-NAME><BUS-DEPENDENT-NM-ECUS><CAN-NM-ECU/></BUS-DEPENDENT-NM-ECUS></NM-ECU>" % NS
        ecu = _parse_ecus(xml)[0]
        assert ecu.getChecksum() is None
        assert ecu.getTimestamp() is None
