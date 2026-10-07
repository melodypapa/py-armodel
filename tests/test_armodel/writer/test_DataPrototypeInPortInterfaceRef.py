"""Writer/reader round-trip tests for DataPrototypeInPortInterfaceRef (Table 7.19, p.788).

Wrapper element names per the XSD group DATA-PROTOTYPE-IN-PORT-INTERFACE-REF
(AUTOSAR_00052.xsd): DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF and
DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF, both after TAG-ID
(XSD complexType sequence: AR-OBJECT, DATA-PROTOTYPE-REFERENCE, own group).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeInSenderReceiverInterfaceInstanceRef,
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


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _full_ref() -> DataPrototypeInPortInterfaceRef:
    ref = DataPrototypeInPortInterfaceRef()
    ref.setTagId(PositiveInteger().setValue("5"))

    cs = DataPrototypeInClientServerInterfaceInstanceRef()
    cs.setBaseRef(_ref("/Cs", "CLIENT-SERVER-INTERFACE"))
    cs.setTargetDataPrototypeInCsRef(_ref("/Cs/MyArg", "DATA-PROTOTYPE"))
    ref.setDataPrototypeInClientServerInterface(cs)

    sr = DataPrototypeInSenderReceiverInterfaceInstanceRef()
    sr.setBaseRef(_ref("/Sr", "SENDER-RECEIVER-INTERFACE"))
    sr.setRootDataPrototypeInSrRef(_ref("/Sr/Root", "AUTOSAR-DATA-PROTOTYPE"))
    sr.setTargetDataPrototypeInSrRef(_ref("/Sr/MyVar", "DATA-PROTOTYPE"))
    ref.setDataPrototypeInSenderReceiverInterface(sr)
    return ref


class TestDataPrototypeInPortInterfaceRefWriter:
    def test_write_cs_and_sr_irefs(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInPortInterfaceRef(parent, _full_ref())

        el = parent.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        assert el is not None
        assert el.find("TAG-ID").text == "5"

        cs_ref = el.find("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        assert cs_ref is not None
        assert cs_ref.find("BASE").text == "/Cs"
        assert cs_ref.find("TARGET-DATA-PROTOTYPE-IN-CS").text == "/Cs/MyArg"

        sr_ref = el.find("DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")
        assert sr_ref is not None
        assert sr_ref.find("BASE") is None
        assert sr_ref.find("ROOT-DATA-PROTOTYPE-IN-SR-REF").text == "/Sr/Root"
        assert sr_ref.find("TARGET-DATA-PROTOTYPE-IN-SR-REF").text == "/Sr/MyVar"

        children = [child.tag for child in el]
        assert children.index("TAG-ID") < children.index("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        assert children.index("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF") < children.index("DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")

    def test_write_empty_ref(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInPortInterfaceRef(parent, DataPrototypeInPortInterfaceRef())

        el = parent.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        assert el is not None
        assert el.find("TAG-ID") is None
        assert el.find("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF") is None
        assert el.find("DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF") is None


class TestDataPrototypeInPortInterfaceRefRoundTrip:
    def test_round_trip_preserves_both_irefs(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInPortInterfaceRef(parent, _full_ref())

        out_file = str(tmp_path / "data_prototype_in_port_interface_ref.arxml")
        inner = ET.tostring(parent[0]).decode("utf-8")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")

        tree = ET.parse(out_file)
        recovered = DataPrototypeInPortInterfaceRef()
        parser.readDataPrototypeInPortInterfaceRef(parser.find(tree.getroot(), "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF"), recovered)

        assert recovered.getTagId() is not None
        assert recovered.getTagId().getValue() == 5

        cs_ref = recovered.getDataPrototypeInClientServerInterface()
        assert isinstance(cs_ref, DataPrototypeInClientServerInterfaceInstanceRef)
        assert cs_ref.getBaseRef() is not None
        assert cs_ref.getBaseRef().getValue() == "/Cs"
        assert cs_ref.getTargetDataPrototypeInCsRef() is not None
        assert cs_ref.getTargetDataPrototypeInCsRef().getValue() == "/Cs/MyArg"

        sr_ref = recovered.getDataPrototypeInSenderReceiverInterface()
        assert isinstance(sr_ref, DataPrototypeInSenderReceiverInterfaceInstanceRef)
        assert sr_ref.getBaseRef() is None
        assert sr_ref.getRootDataPrototypeInSrRef() is not None
        assert sr_ref.getRootDataPrototypeInSrRef().getValue() == "/Sr/Root"
        assert sr_ref.getTargetDataPrototypeInSrRef() is not None
        assert sr_ref.getTargetDataPrototypeInSrRef().getValue() == "/Sr/MyVar"
