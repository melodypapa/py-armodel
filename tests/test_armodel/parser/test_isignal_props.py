"""Parser tests for ISignalProps (Table 6.10, p.323).

Child set and order per the I-SIGNAL-PROPS group of AUTOSAR_00052.xsd (l.67362);
the AR:AR-OBJECT S/T attribute group round-trips through readARObject.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignal
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadISignalProps:
    def test_read_full(self):
        signal = ISignal(None, "ISig1")
        element = ET.fromstring(f"<I-SIGNAL xmlns='{NS}'><I-SIGNAL-PROPS S='cs1' T='2024-01-01T00:00:00Z'>" "<HANDLE-OUT-OF-RANGE>SATURATE</HANDLE-OUT-OF-RANGE>" "</I-SIGNAL-PROPS></I-SIGNAL>")
        ARXMLParser().readISignalProps(element, signal)

        props = signal.getISignalProps()
        assert props is not None
        assert props.getHandleOutOfRange() is not None
        assert props.getHandleOutOfRange().value == "SATURATE"
        assert props.getChecksum().getValue() == "cs1"
        assert props.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_read_empty_wrapper(self):
        signal = ISignal(None, "ISig1")
        element = ET.fromstring(f"<I-SIGNAL xmlns='{NS}'><I-SIGNAL-PROPS/></I-SIGNAL>")
        ARXMLParser().readISignalProps(element, signal)

        props = signal.getISignalProps()
        assert props is not None
        assert props.getHandleOutOfRange() is None
        assert props.getChecksum() is None
        assert props.getTimestamp() is None

    def test_read_absent(self):
        signal = ISignal(None, "ISig1")
        element = ET.fromstring(f"<I-SIGNAL xmlns='{NS}'><SHORT-NAME>ISig1</SHORT-NAME></I-SIGNAL>")
        ARXMLParser().readISignalProps(element, signal)

        assert signal.getISignalProps() is None
