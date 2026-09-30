"""
Tests for reading R-PORT-IN-COMPOSITION-INSTANCE-REF elements — RPortInCompositionInstanceRef, Table D.16 (p.952, R23-11).

RPortInCompositionInstanceRef (Base = PortInCompositionTypeInstanceRef) carries two own
reference elements whose reader element order must follow the XSD sequence
(AUTOSAR_00052.xsd complexType R-PORT-IN-COMPOSITION-INSTANCE-REF):
CONTEXT-COMPONENT-REF → TARGET-R-PORT-REF, plus the AR-OBJECT attributeGroup S/T
attributes round-tripped through readARObject on both aggregation paths
(AssemblySwConnector.requester and DelegationSwConnector.innerPort).

Round-trip counterpart: tests/test_armodel/writer/test_r_port_in_composition_instance_ref.py
"""

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import RPortInCompositionInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from tests.test_armodel.parser._helpers import _snip

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    return ARXMLParser(options={"warning": True})


def _delegation_connector():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createCompositionSwComponentType("Comp").createDelegationSwConnector("DelConn")


def _assembly_connector():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return pkg.createCompositionSwComponentType("Comp").createAssemblySwConnector("AsmConn")


def _r_port_iref_element():
    return _snip(
        "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Comp/Context</CONTEXT-COMPONENT-REF>" "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/Comp/Inner/RPort</TARGET-R-PORT-REF>",
        root_tag="R-PORT-IN-COMPOSITION-INSTANCE-REF",
    )


class TestReadRPortInCompositionInstanceRef:
    """Tests for readRPortInCompositionInstanceRef — own element field values (Table D.16)."""

    def test_read_field_values(self, parser):
        """Test that both reference elements are read with their values and DEST attributes."""
        instance_ref = RPortInCompositionInstanceRef()

        parser.readRPortInCompositionInstanceRef(_r_port_iref_element(), instance_ref)

        context_ref = instance_ref.getContextComponentRef()
        assert context_ref is not None
        assert context_ref.getValue() == "/Comp/Context"
        assert context_ref.getDest() == "SW-COMPONENT-PROTOTYPE"
        target_ref = instance_ref.getTargetRPortRef()
        assert target_ref is not None
        assert target_ref.getValue() == "/Comp/Inner/RPort"
        assert target_ref.getDest() == "R-PORT-PROTOTYPE"

    def test_read_absent_refs(self, parser):
        """Test that absent reference elements leave both fields unset."""
        element = _snip("", root_tag="R-PORT-IN-COMPOSITION-INSTANCE-REF")

        instance_ref = RPortInCompositionInstanceRef()
        parser.readRPortInCompositionInstanceRef(element, instance_ref)

        assert instance_ref.getContextComponentRef() is None
        assert instance_ref.getTargetRPortRef() is None


class TestReadRPortInCompositionInstanceRefARObject:
    """Tests for the AR-OBJECT attributeGroup S/T round-trip on both aggregation paths."""

    def test_read_s_attribute_via_delegation_inner_port(self, parser):
        """Test that the S checksum attribute is read on the DelegationSwConnector.innerPort path."""
        connector_element = _snip(
            "<INNER-PORT-IREF>"
            "<R-PORT-IN-COMPOSITION-INSTANCE-REF S='abc123'>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Comp/Context</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/Comp/Inner/RPort</TARGET-R-PORT-REF>"
            "</R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "</INNER-PORT-IREF>",
            root_tag="DELEGATION-SW-CONNECTOR",
        )
        connector = _delegation_connector()

        parser.readDelegationSwConnectorInnerPortIRef(connector_element, connector)

        inner_port_iref = connector.getInnerPortIRef()
        assert isinstance(inner_port_iref, RPortInCompositionInstanceRef)
        assert inner_port_iref.getContextComponentRef().getValue() == "/Comp/Context"
        assert inner_port_iref.getTargetRPortRef().getValue() == "/Comp/Inner/RPort"
        assert inner_port_iref.getChecksum() is not None
        assert inner_port_iref.getChecksum().getValue() == "abc123"

    def test_read_s_attribute_via_assembly_requester(self, parser):
        """Test that the S checksum attribute is read on the AssemblySwConnector.requester path (REQUESTER-IREF is typed R-PORT-IN-COMPOSITION-INSTANCE-REF per XSD)."""
        connector_element = _snip(
            "<REQUESTER-IREF S='abc123'>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Comp/Context</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/Comp/Inner/RPort</TARGET-R-PORT-REF>"
            "</REQUESTER-IREF>",
            root_tag="ASSEMBLY-SW-CONNECTOR",
        )
        connector = _assembly_connector()

        parser.readAssemblySwConnectorRequesterIRef(connector_element, connector)

        requester_iref = connector.getRequesterIRef()
        assert isinstance(requester_iref, RPortInCompositionInstanceRef)
        assert requester_iref.getContextComponentRef().getValue() == "/Comp/Context"
        assert requester_iref.getTargetRPortRef().getValue() == "/Comp/Inner/RPort"
        assert requester_iref.getChecksum() is not None
        assert requester_iref.getChecksum().getValue() == "abc123"
