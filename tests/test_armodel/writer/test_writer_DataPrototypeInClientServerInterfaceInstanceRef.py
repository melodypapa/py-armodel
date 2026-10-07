"""Writer/reader round-trip tests for DataPrototypeInClientServerInterfaceInstanceRef (Table 7.21, p.788).

Inner element names per the XSD group DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-INSTANCE-REF
(AUTOSAR_00052.xsd), written in XSD sequenceOffset order (ROOT 10, CONTEXT 20, TARGET 30):
ROOT-DATA-PROTOTYPE-IN-CS-REF, CONTEXT-DATA-PROTOTYPE-IN-CS-REF (0..*, flat) and
TARGET-DATA-PROTOTYPE-IN-CS-REF. The `base` association is atpDerived -- never serialized.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInClientServerInterfaceInstanceRef
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


def _full_iref() -> DataPrototypeInClientServerInterfaceInstanceRef:
    iref = DataPrototypeInClientServerInterfaceInstanceRef()
    iref.setBaseRef(_ref("/Cs", "CLIENT-SERVER-INTERFACE"))
    iref.setRootDataPrototypeInCsRef(_ref("/Cs/Root", "ARGUMENT-DATA-PROTOTYPE"))
    iref.addContextDataPrototypeInCsRefs(_ref("/Cs/Root/RecElem", "APPLICATION-RECORD-ELEMENT"))
    iref.addContextDataPrototypeInCsRefs(_ref("/Cs/Root/RecElem/ArrElem", "APPLICATION-ARRAY-ELEMENT"))
    iref.setTargetDataPrototypeInCsRef(_ref("/Cs/MyArg", "DATA-PROTOTYPE"))
    return iref


class TestDataPrototypeInClientServerInterfaceInstanceRefWriter:
    def test_write_full_iref(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInClientServerInterfaceInstanceRef(parent, _full_iref())

        el = parent.find("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        assert el is not None

        root_ref = el.find("ROOT-DATA-PROTOTYPE-IN-CS-REF")
        assert root_ref is not None
        assert root_ref.text == "/Cs/Root"
        assert root_ref.attrib["DEST"] == "ARGUMENT-DATA-PROTOTYPE"

        ctx_refs = el.findall("CONTEXT-DATA-PROTOTYPE-IN-CS-REF")
        assert len(ctx_refs) == 2
        assert ctx_refs[0].text == "/Cs/Root/RecElem"
        assert ctx_refs[0].attrib["DEST"] == "APPLICATION-RECORD-ELEMENT"
        assert ctx_refs[1].text == "/Cs/Root/RecElem/ArrElem"
        assert ctx_refs[1].attrib["DEST"] == "APPLICATION-ARRAY-ELEMENT"

        target_ref = el.find("TARGET-DATA-PROTOTYPE-IN-CS-REF")
        assert target_ref is not None
        assert target_ref.text == "/Cs/MyArg"
        assert target_ref.attrib["DEST"] == "DATA-PROTOTYPE"

        children = [child.tag for child in el]
        assert children.index("ROOT-DATA-PROTOTYPE-IN-CS-REF") < children.index("CONTEXT-DATA-PROTOTYPE-IN-CS-REF")
        assert children.index("CONTEXT-DATA-PROTOTYPE-IN-CS-REF") < children.index("TARGET-DATA-PROTOTYPE-IN-CS-REF")

    def test_write_never_serializes_atp_derived_base(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInClientServerInterfaceInstanceRef(parent, _full_iref())

        el = parent.find("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        assert el.find("BASE") is None
        assert el.find("BASE-REF") is None

    def test_write_empty_iref(self, writer):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInClientServerInterfaceInstanceRef(parent, DataPrototypeInClientServerInterfaceInstanceRef())

        el = parent.find("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        assert el is not None
        assert el.find("ROOT-DATA-PROTOTYPE-IN-CS-REF") is None
        assert el.find("CONTEXT-DATA-PROTOTYPE-IN-CS-REF") is None
        assert el.find("TARGET-DATA-PROTOTYPE-IN-CS-REF") is None


class TestDataPrototypeInClientServerInterfaceInstanceRefRoundTrip:
    def test_round_trip_preserves_all_refs(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.writeDataPrototypeInClientServerInterfaceInstanceRef(parent, _full_iref())

        out_file = str(tmp_path / "data_prototype_in_cs_interface_instance_ref.arxml")
        inner = ET.tostring(parent[0]).decode("utf-8")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")

        tree = ET.parse(out_file)
        recovered = DataPrototypeInClientServerInterfaceInstanceRef()
        parser.readDataPrototypeInClientServerInterfaceInstanceRef(parser.find(tree.getroot(), "DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF"), recovered)

        assert recovered.getBaseRef() is None
        assert recovered.getRootDataPrototypeInCsRef() is not None
        assert recovered.getRootDataPrototypeInCsRef().getValue() == "/Cs/Root"
        assert recovered.getRootDataPrototypeInCsRef().getDest() == "ARGUMENT-DATA-PROTOTYPE"

        ctx_refs = recovered.getContextDataPrototypeInCsRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/Cs/Root/RecElem"
        assert ctx_refs[1].getValue() == "/Cs/Root/RecElem/ArrElem"

        assert recovered.getTargetDataPrototypeInCsRef() is not None
        assert recovered.getTargetDataPrototypeInCsRef().getValue() == "/Cs/MyArg"
