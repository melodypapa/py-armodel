"""
Tests for writing R-PORT-IN-COMPOSITION-INSTANCE-REF elements — RPortInCompositionInstanceRef, Table D.16 (p.952, R23-11).

RPortInCompositionInstanceRef (Base = PortInCompositionTypeInstanceRef) carries two own
reference elements whose writer element order must follow the XSD sequence
(AUTOSAR_00052.xsd complexType R-PORT-IN-COMPOSITION-INSTANCE-REF):
CONTEXT-COMPONENT-REF → TARGET-R-PORT-REF, plus the AR-OBJECT attributeGroup S/T
attributes emitted through writeARObject on both aggregation paths
(AssemblySwConnector.requester and DelegationSwConnector.innerPort).

Round-trip counterpart: tests/test_armodel/parser/test_r_port_in_composition_instance_ref.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import RPortInCompositionInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "CONTEXT-COMPONENT-REF",
    "TARGET-R-PORT-REF",
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
    return ARXMLWriter()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    return ARXMLParser(options={"warning": True})


def _context_ref():
    ref = RefType()
    ref.setValue("/Comp/Context")
    ref.setDest("SW-COMPONENT-PROTOTYPE")
    return ref


def _target_r_port_ref():
    ref = RefType()
    ref.setValue("/Comp/Inner/RPort")
    ref.setDest("R-PORT-PROTOTYPE")
    return ref


def _filled_iref():
    iref = RPortInCompositionInstanceRef()
    iref.setContextComponentRef(_context_ref())
    iref.setTargetRPortRef(_target_r_port_ref())
    return iref


def _delegation_connector_under(pkg_name="Pkg", comp_name="Comp", conn_name="DelConn"):
    pkg = AUTOSAR.getInstance().createARPackage(pkg_name)
    return pkg.createCompositionSwComponentType(comp_name).createDelegationSwConnector(conn_name)


def _assembly_connector_under(pkg_name="Pkg", comp_name="Comp", conn_name="AsmConn"):
    pkg = AUTOSAR.getInstance().createARPackage(pkg_name)
    return pkg.createCompositionSwComponentType(comp_name).createAssemblySwConnector(conn_name)


class TestWriteRPortInCompositionInstanceRef:
    """Tests for writeRPortInCompositionInstanceRef — own element field values (Table D.16)."""

    def test_write_field_values(self, writer):
        """Test that both reference elements are emitted with their values read through the getters."""
        element = ET.Element("R-PORT-IN-COMPOSITION-INSTANCE-REF")

        writer.writeRPortInCompositionInstanceRef(element, _filled_iref())

        context_ref = element.find("CONTEXT-COMPONENT-REF")
        assert context_ref.text == "/Comp/Context"
        assert context_ref.attrib.get("DEST") == "SW-COMPONENT-PROTOTYPE"
        target_ref = element.find("TARGET-R-PORT-REF")
        assert target_ref.text == "/Comp/Inner/RPort"
        assert target_ref.attrib.get("DEST") == "R-PORT-PROTOTYPE"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD sequenceOffset order."""
        element = ET.Element("R-PORT-IN-COMPOSITION-INSTANCE-REF")

        writer.writeRPortInCompositionInstanceRef(element, _filled_iref())

        assert [child.tag for child in element] == XSD_ELEMENT_ORDER

    def test_write_unset_iref_emits_no_children(self, writer):
        """Test that an instance ref without fields emits no attribute children."""
        element = ET.Element("R-PORT-IN-COMPOSITION-INSTANCE-REF")

        writer.writeRPortInCompositionInstanceRef(element, RPortInCompositionInstanceRef())

        assert element.find("CONTEXT-COMPONENT-REF") is None
        assert element.find("TARGET-R-PORT-REF") is None

    def test_write_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are emitted."""
        iref = _filled_iref()
        checksum = String()
        checksum.setValue("abc123")
        iref.setChecksum(checksum)

        element = ET.Element("R-PORT-IN-COMPOSITION-INSTANCE-REF")
        writer.writeRPortInCompositionInstanceRef(element, iref)

        assert element.attrib.get("S") == "abc123"

    def test_write_s_attribute_via_delegation_inner_port(self, writer):
        """Test that the S checksum attribute is emitted on the DelegationSwConnector.innerPort path."""
        connector = _delegation_connector_under()
        iref = _filled_iref()
        checksum = String()
        checksum.setValue("abc123")
        iref.setChecksum(checksum)
        connector.setInnerPortIRef(iref)

        parent = ET.Element("PARENT")
        writer.writeDelegationSwConnector(parent, connector)

        instance_ref = parent.find("DELEGATION-SW-CONNECTOR/INNER-PORT-IREF/R-PORT-IN-COMPOSITION-INSTANCE-REF")
        assert instance_ref is not None
        assert instance_ref.attrib.get("S") == "abc123"
        assert instance_ref.find("CONTEXT-COMPONENT-REF").text == "/Comp/Context"
        assert instance_ref.find("TARGET-R-PORT-REF").text == "/Comp/Inner/RPort"

    def test_write_s_attribute_via_assembly_requester(self, writer):
        """Test that the S checksum attribute is emitted on the AssemblySwConnector.requester path."""
        connector = _assembly_connector_under()
        iref = _filled_iref()
        checksum = String()
        checksum.setValue("abc123")
        iref.setChecksum(checksum)
        connector.setRequesterIRef(iref)

        parent = ET.Element("PARENT")
        writer.writeAssemblySwConnector(parent, connector)

        requester_iref = parent.find("ASSEMBLY-SW-CONNECTOR/REQUESTER-IREF")
        assert requester_iref is not None
        assert requester_iref.attrib.get("S") == "abc123"
        assert requester_iref.find("CONTEXT-COMPONENT-REF").text == "/Comp/Context"
        assert requester_iref.find("TARGET-R-PORT-REF").text == "/Comp/Inner/RPort"


class TestRPortInCompositionInstanceRefRoundTrip:
    """Write → reparse round-trips for both aggregation paths."""

    def test_round_trip_via_delegation_inner_port(self, writer, parser):
        """Test the writeDelegationSwConnector → readDelegationSwConnectorInnerPortIRef round-trip with field values and S/T."""
        connector = _delegation_connector_under()
        iref = _filled_iref()
        checksum = String()
        checksum.setValue("abc123")
        iref.setChecksum(checksum)
        connector.setInnerPortIRef(iref)

        parent = ET.Element("PARENT")
        writer.writeDelegationSwConnector(parent, connector)
        element = parent.find("DELEGATION-SW-CONNECTOR")
        assert element is not None
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("DELEGATION-SW-CONNECTOR", "DELEGATION-SW-CONNECTOR xmlns='%s'" % NS, 1))

        reparsed = _delegation_connector_under("Pkg2", "Comp2", "DelConn2")
        parser.readDelegationSwConnectorInnerPortIRef(reloaded_element, reparsed)

        inner_port_iref = reparsed.getInnerPortIRef()
        assert isinstance(inner_port_iref, RPortInCompositionInstanceRef)
        assert inner_port_iref.getContextComponentRef().getValue() == "/Comp/Context"
        assert inner_port_iref.getContextComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert inner_port_iref.getTargetRPortRef().getValue() == "/Comp/Inner/RPort"
        assert inner_port_iref.getTargetRPortRef().getDest() == "R-PORT-PROTOTYPE"
        assert inner_port_iref.getChecksum() is not None
        assert inner_port_iref.getChecksum().getValue() == "abc123"

    def test_round_trip_via_assembly_requester(self, writer, parser):
        """Test the writeAssemblySwConnector → readAssemblySwConnectorRequesterIRef round-trip with field values and S/T."""
        connector = _assembly_connector_under()
        iref = _filled_iref()
        checksum = String()
        checksum.setValue("abc123")
        iref.setChecksum(checksum)
        connector.setRequesterIRef(iref)

        parent = ET.Element("PARENT")
        writer.writeAssemblySwConnector(parent, connector)
        element = parent.find("ASSEMBLY-SW-CONNECTOR")
        assert element is not None
        xml_text = ET.tostring(element, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("ASSEMBLY-SW-CONNECTOR", "ASSEMBLY-SW-CONNECTOR xmlns='%s'" % NS, 1))

        reparsed = _assembly_connector_under("Pkg2", "Comp2", "AsmConn2")
        parser.readAssemblySwConnectorRequesterIRef(reloaded_element, reparsed)

        requester_iref = reparsed.getRequesterIRef()
        assert isinstance(requester_iref, RPortInCompositionInstanceRef)
        assert requester_iref.getContextComponentRef().getValue() == "/Comp/Context"
        assert requester_iref.getTargetRPortRef().getValue() == "/Comp/Inner/RPort"
        assert requester_iref.getChecksum() is not None
        assert requester_iref.getChecksum().getValue() == "abc123"
