"""
Tests for writing AUTOSAR-VARIABLE-REF elements — AutosarVariableRef, Table 5.33 (p.316, R23-11).

AutosarVariableRef (Base = ARObject) carries three own attributes whose writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd group AUTOSAR-VARIABLE-REF):
AUTOSAR-VARIABLE-IN-IMPL-DATATYPE → AUTOSAR-VARIABLE-IREF → LOCAL-VARIABLE-REF. The
ACCESSED-VARIABLE element is emitted only when the reference is set. The set-level
round-trip goes through the VariableAccess aggregation (writeVariableAccess dispatch →
readVariableAccess dispatch).

Round-trip counterpart: tests/test_armodel/parser/test_autosar_variable_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ArVariableInImplementationDataInstanceRef,
    AutosarVariableRef,
    VariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
    VariableInAtomicSWCTypeInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "AUTOSAR-VARIABLE-IN-IMPL-DATATYPE",
    "AUTOSAR-VARIABLE-IREF",
    "LOCAL-VARIABLE-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _filled_variable_ref():
    ref = AutosarVariableRef()

    impl = ArVariableInImplementationDataInstanceRef()
    impl.setPortPrototypeRef(_ref("/ImplPort", "PORT-PROTOTYPE"))
    impl.setRootVariableDataPrototypeRef(_ref("/RootVariable", "VARIABLE-DATA-PROTOTYPE"))
    impl.addContextDataPrototypeRef(_ref("/Ctx1", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    impl.addContextDataPrototypeRef(_ref("/Ctx2", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    impl.setTargetDataPrototypeRef(_ref("/ImplTarget", "IMPLEMENTATION-DATA-TYPE-ELEMENT"))
    ref.setAutosarVariableInImplDatatype(impl)

    iref = VariableInAtomicSWCTypeInstanceRef()
    iref.setPortPrototypeRef(_ref("/VarPort", "PORT-PROTOTYPE"))
    iref.setTargetDataPrototypeRef(_ref("/VarTarget", "VARIABLE-DATA-PROTOTYPE"))
    ref.setAutosarVariableIRef(iref)

    ref.setLocalVariableRef(_ref("/LocalVariable", "VARIABLE-DATA-PROTOTYPE"))
    return ref


class TestWriteAutosarVariableRef:
    """Tests for setAutosarVariableRef — own element field values (Table 5.33)."""

    def test_write_field_values(self, writer):
        """Test that all three attribute elements are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.setAutosarVariableRef(parent, "AUTOSAR-VARIABLE-REF", _filled_variable_ref())

        element = parent.find("AUTOSAR-VARIABLE-REF")
        assert element is not None
        impl_element = element.find("AUTOSAR-VARIABLE-IN-IMPL-DATATYPE")
        assert impl_element is not None
        assert impl_element.find("PORT-PROTOTYPE-REF").text == "/ImplPort"
        assert impl_element.find("ROOT-VARIABLE-DATA-PROTOTYPE-REF").text == "/RootVariable"
        contexts = impl_element.findall("CONTEXT-DATA-PROTOTYPE-REF")
        assert [ctx.text for ctx in contexts] == ["/Ctx1", "/Ctx2"]
        assert impl_element.find("TARGET-DATA-PROTOTYPE-REF").text == "/ImplTarget"
        iref_element = element.find("AUTOSAR-VARIABLE-IREF")
        assert iref_element is not None
        assert iref_element.find("PORT-PROTOTYPE-REF").text == "/VarPort"
        assert iref_element.find("TARGET-DATA-PROTOTYPE-REF").text == "/VarTarget"
        local_element = element.find("LOCAL-VARIABLE-REF")
        assert local_element.text == "/LocalVariable"
        assert local_element.attrib.get("DEST") == "VARIABLE-DATA-PROTOTYPE"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group sequenceOffset order."""
        parent = ET.Element("PARENT")

        writer.setAutosarVariableRef(parent, "AUTOSAR-VARIABLE-REF", _filled_variable_ref())

        element = parent.find("AUTOSAR-VARIABLE-REF")
        assert [elem.tag for elem in element] == XSD_ELEMENT_ORDER

    def test_write_unset_ref_emits_no_children(self, writer):
        """Test that a reference without fields emits the element only, with no attribute children."""
        parent = ET.Element("PARENT")

        writer.setAutosarVariableRef(parent, "AUTOSAR-VARIABLE-REF", AutosarVariableRef())

        element = parent.find("AUTOSAR-VARIABLE-REF")
        assert element is not None
        assert element.find("AUTOSAR-VARIABLE-IN-IMPL-DATATYPE") is None
        assert element.find("AUTOSAR-VARIABLE-IREF") is None
        assert element.find("LOCAL-VARIABLE-REF") is None

    def test_write_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are emitted."""
        ref = AutosarVariableRef()
        checksum = String()
        checksum.setValue("abc123")
        ref.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        ref.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.setAutosarVariableRef(parent, "AUTOSAR-VARIABLE-REF", ref)

        element = parent.find("AUTOSAR-VARIABLE-REF")
        assert element.attrib.get("S") == "abc123"
        assert element.attrib.get("T") is not None


class TestVariableAccessRoundTrip:
    """Tests for the VariableAccess.accessedVariable aggregation round-trip."""

    def test_round_trip_via_variable_access(self, writer):
        """Test the writeVariableAccess → readVariableAccess aggregation round-trip with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = VariableAccess(root, "VarAccess")
        access.setAccessedVariable(_filled_variable_ref())

        parent = ET.Element("PARENT")
        writer.writeVariableAccess(parent, access)

        element = parent.find("VARIABLE-ACCESS")
        assert element is not None
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("VARIABLE-ACCESS", "VARIABLE-ACCESS xmlns='%s'" % NS, 1))

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        reloaded = VariableAccess(root2, "OtherName")
        ARXMLParser().readVariableAccess(reloaded_element, reloaded)

        ref = reloaded.getAccessedVariable()
        assert isinstance(ref, AutosarVariableRef)
        assert ref.getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/VarPort"
        assert ref.getAutosarVariableIRef().getTargetDataPrototypeRef().getValue() == "/VarTarget"
        impl = ref.getAutosarVariableInImplDatatype()
        assert impl.getRootVariableDataPrototypeRef().getValue() == "/RootVariable"
        assert [ctx.getValue() for ctx in impl.getContextDataPrototypeRefs()] == ["/Ctx1", "/Ctx2"]
        assert ref.getLocalVariableRef().getValue() == "/LocalVariable"
        assert ref.getLocalVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_round_trip_absent_accessed_variable_emits_no_element(self, writer):
        """Test that a VariableAccess without an accessed variable emits no ACCESSED-VARIABLE element."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = VariableAccess(root, "VarAccess")

        parent = ET.Element("PARENT")
        writer.writeVariableAccess(parent, access)

        element = parent.find("VARIABLE-ACCESS")
        assert element.find("ACCESSED-VARIABLE") is None
