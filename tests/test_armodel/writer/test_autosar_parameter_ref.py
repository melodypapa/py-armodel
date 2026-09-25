"""
Tests for writing AUTOSAR-PARAMETER-REF elements — AutosarParameterRef, Table 5.34 (p.317, R23-11).

AutosarParameterRef (Base = ARObject) carries two own attributes whose writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd group AUTOSAR-PARAMETER-REF):
AUTOSAR-PARAMETER-IREF → LOCAL-PARAMETER-REF. The ARObject base attributes (S checksum,
T timestamp) belong to the element set via the XSD AR-OBJECT attributeGroup. The
PARAMETER-ACCESS wrapper is emitted by writeParameterAccess; its round-trip goes through
readParameterAccess.

Round-trip counterpart: tests/test_armodel/parser/test_autosar_parameter_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, ParameterAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "AUTOSAR-PARAMETER-IREF",
    "LOCAL-PARAMETER-REF",
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


def _filled_parameter_ref():
    parameter = AutosarParameterRef()
    iref = ParameterInAtomicSWCTypeInstanceRef()

    port_ref = RefType()
    port_ref.setValue("/Swc/Port")
    port_ref.setDest("PORT-PROTOTYPE")
    iref.setPortPrototypeRef(port_ref)
    root_ref = RefType()
    root_ref.setValue("/Swc/RootParameter")
    root_ref.setDest("PARAMETER-DATA-PROTOTYPE")
    iref.setRootParameterDataPrototypeRef(root_ref)
    target_ref = RefType()
    target_ref.setValue("/Swc/TargetElement")
    target_ref.setDest("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE")
    iref.setTargetDataPrototypeRef(target_ref)
    parameter.setAutosarParameterIRef(iref)

    local_ref = RefType()
    local_ref.setValue("/Swc/LocalParameter")
    local_ref.setDest("PARAMETER-DATA-PROTOTYPE")
    parameter.setLocalParameterRef(local_ref)
    return parameter


class TestWriteAutosarParameterRef:
    """Tests for setAutosarParameterRef — own element field values (Table 5.34)."""

    def test_write_field_values(self, writer):
        """Test that both attribute elements are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", _filled_parameter_ref())

        element = parent.find("ACCESSED-PARAMETER")
        assert element is not None
        iref_element = element.find("AUTOSAR-PARAMETER-IREF")
        assert iref_element is not None
        port_ref_element = iref_element.find("PORT-PROTOTYPE-REF")
        assert port_ref_element.text == "/Swc/Port"
        assert port_ref_element.attrib.get("DEST") == "PORT-PROTOTYPE"
        assert iref_element.find("ROOT-PARAMETER-DATA-PROTOTYPE-REF").text == "/Swc/RootParameter"
        assert iref_element.find("TARGET-DATA-PROTOTYPE-REF").text == "/Swc/TargetElement"
        local_ref_element = element.find("LOCAL-PARAMETER-REF")
        assert local_ref_element.text == "/Swc/LocalParameter"
        assert local_ref_element.attrib.get("DEST") == "PARAMETER-DATA-PROTOTYPE"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group sequenceOffset order."""
        parent = ET.Element("PARENT")

        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", _filled_parameter_ref())

        element = parent.find("ACCESSED-PARAMETER")
        assert [elem.tag for elem in element] == XSD_ELEMENT_ORDER

    def test_write_unset_parameter_ref_emits_no_children(self, writer):
        """Test that a parameter ref without fields emits the element only, with no attribute children."""
        parent = ET.Element("PARENT")

        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", AutosarParameterRef())

        element = parent.find("ACCESSED-PARAMETER")
        assert element is not None
        assert element.find("AUTOSAR-PARAMETER-IREF") is None
        assert element.find("LOCAL-PARAMETER-REF") is None

    def test_write_none_emits_nothing(self, writer):
        """Test that a None parameter ref emits no element at all."""
        parent = ET.Element("PARENT")

        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", None)

        assert len(parent) == 0

    def test_write_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are emitted."""
        parameter = AutosarParameterRef()
        checksum = String()
        checksum.setValue("abc123")
        parameter.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        parameter.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", parameter)

        element = parent.find("ACCESSED-PARAMETER")
        assert element.attrib.get("S") == "abc123"
        assert element.attrib.get("T") is not None


class TestAutosarParameterRefRoundTrip:
    """Tests for the aggregation round-trips."""

    def _reparse(self, parent_element, root_tag):
        xml_text = ET.tostring(parent_element, encoding="unicode")
        return ET.fromstring(xml_text.replace(root_tag, f"{root_tag} xmlns='{NS}'", 1))

    def test_round_trip_via_parameter_access(self, writer):
        """Test the parameter access aggregation round-trip with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        access = ParameterAccess(root, "Pa1")
        access.setAccessedParameter(_filled_parameter_ref())

        parent = ET.Element("PARENT")
        writer.writeParameterAccess(parent, access)

        element = parent.find("PARAMETER-ACCESS")
        assert element is not None
        reloaded_element = self._reparse(element, "PARAMETER-ACCESS")

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        reloaded = ParameterAccess(root2, "OtherName")
        ARXMLParser().readParameterAccess(reloaded_element, reloaded)

        parameter = reloaded.getAccessedParameter()
        assert isinstance(parameter, AutosarParameterRef)
        iref = parameter.getAutosarParameterIRef()
        assert isinstance(iref, ParameterInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/Port"
        assert iref.getPortPrototypeRef().getDest() == "PORT-PROTOTYPE"
        assert iref.getRootParameterDataPrototypeRef().getValue() == "/Swc/RootParameter"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Swc/TargetElement"
        assert parameter.getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        assert parameter.getLocalParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_round_trip_own_element(self, writer):
        """Test the own-element round-trip with field values, incl. an absent-element case."""
        parent = ET.Element("PARENT")
        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", _filled_parameter_ref())

        reloaded_element = self._reparse(parent, "PARENT")
        reloaded = ARXMLParser().getAutosarParameterRef(reloaded_element, "ACCESSED-PARAMETER")

        assert reloaded is not None
        assert reloaded.getAutosarParameterIRef().getTargetDataPrototypeRef().getValue() == "/Swc/TargetElement"
        assert reloaded.getLocalParameterRef().getValue() == "/Swc/LocalParameter"

    def test_round_trip_unset_parameter_ref_emits_no_children(self, writer):
        """Test that an unset parameter ref round-trips to an instance with all fields unset."""
        parent = ET.Element("PARENT")
        writer.setAutosarParameterRef(parent, "ACCESSED-PARAMETER", AutosarParameterRef())

        reloaded_element = self._reparse(parent, "PARENT")
        reloaded = ARXMLParser().getAutosarParameterRef(reloaded_element, "ACCESSED-PARAMETER")

        assert reloaded is not None
        assert reloaded.getAutosarParameterIRef() is None
        assert reloaded.getLocalParameterRef() is None
