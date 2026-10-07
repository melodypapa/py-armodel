"""Writer round-trip tests for SwcToSwcSignal (Table 5.37, p.253).

Serialized through the SWC-TO-SWC-SIGNAL element
(XSD group SWC-TO-SWC-SIGNAL, AUTOSAR_00052.xsd l.118172:
DATA-ELEMENT-IREFS wrapper emitted only when non-empty).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcSignal
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSwcToSwcSignal:
    def test_empty_no_wrapper(self):
        signal = SwcToSwcSignal()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcSignal(parent, signal)

        node = parent.find("SWC-TO-SWC-SIGNAL")
        assert node is not None
        assert node.find("DATA-ELEMENT-IREFS") is None

    def test_full(self):
        signal = SwcToSwcSignal()
        iref1 = VariableDataPrototypeInSystemInstanceRef()
        iref1.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref1.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        iref2 = VariableDataPrototypeInSystemInstanceRef()
        iref2.setTargetDataPrototypeRef(_ref("/Root/SwcB/Vdp2", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref1)
        signal.addDataElementIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcSignal(parent, signal)

        node = parent.find("SWC-TO-SWC-SIGNAL")
        wrapper = node.find("DATA-ELEMENT-IREFS")
        assert wrapper is not None
        items = wrapper.findall("DATA-ELEMENT-IREF")
        assert len(items) == 2
        assert items[0].find("TARGET-DATA-PROTOTYPE-REF").text == "/Root/SwcA/Vdp1"
        assert items[0].find("TARGET-DATA-PROTOTYPE-REF").get("DEST") == "VARIABLE-DATA-PROTOTYPE"
        assert items[1].find("TARGET-DATA-PROTOTYPE-REF").text == "/Root/SwcB/Vdp2"

    def test_round_trip_full(self):
        signal = SwcToSwcSignal()
        iref1 = VariableDataPrototypeInSystemInstanceRef()
        iref1.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref1.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        iref2 = VariableDataPrototypeInSystemInstanceRef()
        iref2.setTargetDataPrototypeRef(_ref("/Root/SwcB/Vdp2", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref1)
        signal.addDataElementIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcSignal(parent, signal)

        reloaded = SwcToSwcSignal()
        ARXMLParser().readSwcToSwcSignal(_with_ns(parent)[0], reloaded)

        irefs = reloaded.getDataElementIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/Root"
        assert irefs[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"
        assert irefs[0].getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert irefs[1].getTargetDataPrototypeRef().getValue() == "/Root/SwcB/Vdp2"

    def test_round_trip_empty(self):
        signal = SwcToSwcSignal()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcSignal(parent, signal)

        reloaded = SwcToSwcSignal()
        ARXMLParser().readSwcToSwcSignal(_with_ns(parent)[0], reloaded)
        assert reloaded.getDataElementIRefs() == []
