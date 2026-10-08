"""Writer/reader round-trip tests for DataPrototypeInSenderReceiverInterfaceInstanceRef (Table 7.20, p.788).

Inner element names per the XSD group DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-INSTANCE-REF
(AUTOSAR_00052.xsd), written in XSD sequenceOffset order (ROOT 10, CONTEXT 20, TARGET 30):
ROOT-DATA-PROTOTYPE-IN-SR-REF, CONTEXT-DATA-PROTOTYPE-IN-SR-REF (0..*, flat) and
TARGET-DATA-PROTOTYPE-IN-SR-REF. The `base` association is atpDerived -- never serialized.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInSenderReceiverInterfaceInstanceRef
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


def _full_iref() -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
    iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
    iref.setBaseRef(_ref("/Sr", "SENDER-RECEIVER-INTERFACE"))
    iref.setRootDataPrototypeInSrRef(_ref("/Sr/Root", "AUTOSAR-DATA-PROTOTYPE"))
    iref.addContextDataPrototypeInSrRefs(_ref("/Sr/Root/RecElem", "APPLICATION-RECORD-ELEMENT"))
    iref.addContextDataPrototypeInSrRefs(_ref("/Sr/Root/RecElem/ArrElem", "APPLICATION-ARRAY-ELEMENT"))
    iref.setTargetDataPrototypeInSrRef(_ref("/Sr/MyVar", "DATA-PROTOTYPE"))
    return iref


class TestDataPrototypeInSenderReceiverInterfaceInstanceRefWriter:
    def test_write_full_iref(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInSenderReceiverInterfaceInstanceRef(parent, _full_iref())

        el = parent.find("DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")
        assert el is not None

        root_ref = el.find("ROOT-DATA-PROTOTYPE-IN-SR-REF")
        assert root_ref is not None
        assert root_ref.text == "/Sr/Root"
        assert root_ref.attrib["DEST"] == "AUTOSAR-DATA-PROTOTYPE"

        ctx_refs = el.findall("CONTEXT-DATA-PROTOTYPE-IN-SR-REF")
        assert len(ctx_refs) == 2
        assert ctx_refs[0].text == "/Sr/Root/RecElem"
        assert ctx_refs[0].attrib["DEST"] == "APPLICATION-RECORD-ELEMENT"
        assert ctx_refs[1].text == "/Sr/Root/RecElem/ArrElem"
        assert ctx_refs[1].attrib["DEST"] == "APPLICATION-ARRAY-ELEMENT"

        target_ref = el.find("TARGET-DATA-PROTOTYPE-IN-SR-REF")
        assert target_ref is not None
        assert target_ref.text == "/Sr/MyVar"
        assert target_ref.attrib["DEST"] == "DATA-PROTOTYPE"

        children = [child.tag for child in el]
        assert children.index("ROOT-DATA-PROTOTYPE-IN-SR-REF") < children.index("CONTEXT-DATA-PROTOTYPE-IN-SR-REF")
        assert children.index("CONTEXT-DATA-PROTOTYPE-IN-SR-REF") < children.index("TARGET-DATA-PROTOTYPE-IN-SR-REF")

    def test_write_never_serializes_atp_derived_base(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInSenderReceiverInterfaceInstanceRef(parent, _full_iref())

        el = parent.find("DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")
        assert el.find("BASE") is None
        assert el.find("BASE-REF") is None

    def test_write_empty_iref(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInSenderReceiverInterfaceInstanceRef(parent, DataPrototypeInSenderReceiverInterfaceInstanceRef())

        el = parent.find("DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")
        assert el is not None
        assert el.find("ROOT-DATA-PROTOTYPE-IN-SR-REF") is None
        assert el.find("CONTEXT-DATA-PROTOTYPE-IN-SR-REF") is None
        assert el.find("TARGET-DATA-PROTOTYPE-IN-SR-REF") is None


class TestDataPrototypeInSenderReceiverInterfaceInstanceRefRoundTrip:
    def test_round_trip_preserves_all_refs(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInSenderReceiverInterfaceInstanceRef(parent, _full_iref())

        out_file = str(tmp_path / "data_prototype_in_sr_interface_instance_ref.arxml")
        inner = ET.tostring(parent[0]).decode("utf-8")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")

        tree = ET.parse(out_file)
        recovered = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        parser.readDataPrototypeInSenderReceiverInterfaceInstanceRef(parser.find(tree.getroot(), "DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF"), recovered)

        assert recovered.getBaseRef() is None
        assert recovered.getRootDataPrototypeInSrRef() is not None
        assert recovered.getRootDataPrototypeInSrRef().getValue() == "/Sr/Root"
        assert recovered.getRootDataPrototypeInSrRef().getDest() == "AUTOSAR-DATA-PROTOTYPE"

        ctx_refs = recovered.getContextDataPrototypeInSrRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/Sr/Root/RecElem"
        assert ctx_refs[1].getValue() == "/Sr/Root/RecElem/ArrElem"

        assert recovered.getTargetDataPrototypeInSrRef() is not None
        assert recovered.getTargetDataPrototypeInSrRef().getValue() == "/Sr/MyVar"
