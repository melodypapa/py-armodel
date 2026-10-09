"""Writer round-trip tests for ISignalProps (Table 6.10, p.323).

Serialized through the aggregator's I-SIGNAL-PROPS element; child order per the
I-SIGNAL-PROPS group of AUTOSAR_00052.xsd (l.67362); the AR:AR-OBJECT S/T
attribute group round-trips through writeARObject/readARObject.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleOutOfRangeEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignal,
    ISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _populate(props: ISignalProps):
    handle = HandleOutOfRangeEnum()
    handle.setValue(HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT)
    props.setHandleOutOfRange(handle)
    props.setChecksum(String().setValue("cs1"))
    props.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))


class TestWriteISignalProps:
    def test_write_full(self):
        signal = ISignal(None, "ISig1")
        props = ISignalProps()
        _populate(props)
        signal.setISignalProps(props)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalProps(parent, signal)

        node = parent.find("I-SIGNAL-PROPS")
        assert node is not None
        assert node.find("HANDLE-OUT-OF-RANGE").text == "EXTERNAL-REPLACEMENT"
        assert node.get("S") == "cs1"
        assert node.get("T") == "2024-01-01T00:00:00Z"

    def test_write_unset_handle(self):
        signal = ISignal(None, "ISig1")
        signal.setISignalProps(ISignalProps())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalProps(parent, signal)

        node = parent.find("I-SIGNAL-PROPS")
        assert node is not None
        assert node.find("HANDLE-OUT-OF-RANGE") is None

    def test_write_absent(self):
        signal = ISignal(None, "ISig1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalProps(parent, signal)

        assert parent.find("I-SIGNAL-PROPS") is None

    def test_round_trip_full(self):
        signal = ISignal(None, "ISig1")
        props = ISignalProps()
        _populate(props)
        signal.setISignalProps(props)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalProps(parent, signal)

        reloaded = ISignal(None, "ISig1")
        ARXMLParser().readISignalProps(_with_ns(parent), reloaded)

        round_tripped = reloaded.getISignalProps()
        assert round_tripped is not None
        assert round_tripped.getHandleOutOfRange() is not None
        assert round_tripped.getHandleOutOfRange().value == "EXTERNAL-REPLACEMENT"
        assert round_tripped.getChecksum().getValue() == "cs1"
        assert round_tripped.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_round_trip_empty(self):
        signal = ISignal(None, "ISig1")
        signal.setISignalProps(ISignalProps())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalProps(parent, signal)

        reloaded = ISignal(None, "ISig1")
        ARXMLParser().readISignalProps(_with_ns(parent), reloaded)

        round_tripped = reloaded.getISignalProps()
        assert round_tripped is not None
        assert round_tripped.getHandleOutOfRange() is None
        assert round_tripped.getChecksum() is None
        assert round_tripped.getTimestamp() is None
