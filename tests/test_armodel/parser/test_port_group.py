"""Reader round-trip tests for PortGroup (value-level, R23-11 Table 4.94)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


NS = "http://autosar.org/schema/r4.0"


def _pg(inner: str) -> ET.Element:
    return ET.fromstring("<PORT-GROUP xmlns='%s'>%s</PORT-GROUP>" % (NS, inner))


def _comp():
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    return pkg.createCompositionSwComponentType("Comp")


def test_read_port_group_values(parser):
    """PORT-GROUP children (INNER-GROUP-IREF / PORT-PROTOTYPE-REF) are read into the model with their values."""
    comp = _comp()
    element = _pg(
        """
            <SHORT-NAME>PG</SHORT-NAME>
            <INNER-GROUP-IREFS>
                <INNER-GROUP-IREF>
                    <TARGET-REF DEST="PORT-GROUP">/Pkg/InnerGroup</TARGET-REF>
                </INNER-GROUP-IREF>
            </INNER-GROUP-IREFS>
            <OUTER-PORTS>
                <PORT-PROTOTYPE-REF-CONDITIONAL>
                    <PORT-PROTOTYPE-REF DEST="PORT-PROTOTYPE">/Pkg/OuterPort</PORT-PROTOTYPE-REF>
                </PORT-PROTOTYPE-REF-CONDITIONAL>
            </OUTER-PORTS>
        """
    )
    parser.readPortGroup(element, comp)
    pg = comp.getPortGroups()[0]
    assert pg.getShortName() == "PG"
    assert len(pg.getInnerGroupIRefs()) == 1
    assert pg.getInnerGroupIRefs()[0].getTargetRef().getValue() == "/Pkg/InnerGroup"
    assert len(pg.getOuterPortRefs()) == 1
    assert pg.getOuterPortRefs()[0].getValue() == "/Pkg/OuterPort"


def test_read_port_group_empty_wrapper(parser):
    """A PORT-GROUP with no inner/outer children yields empty lists (no silent fabrication)."""
    comp = _comp()
    element = _pg("<SHORT-NAME>PG</SHORT-NAME>")
    parser.readPortGroup(element, comp)
    pg = comp.getPortGroups()[0]
    assert pg.getInnerGroupIRefs() == []
    assert pg.getOuterPortRefs() == []


def test_inner_group_iref_instance_ref_type(parser):
    """INNER-GROUP-IREF is modeled as an InnerPortGroupInCompositionInstanceRef."""
    comp = _comp()
    element = _pg(
        """
            <SHORT-NAME>PG</SHORT-NAME>
            <INNER-GROUP-IREFS>
                <INNER-GROUP-IREF>
                    <TARGET-REF DEST="PORT-GROUP">/Pkg/InnerGroup</TARGET-REF>
                </INNER-GROUP-IREF>
            </INNER-GROUP-IREFS>
        """
    )
    parser.readPortGroup(element, comp)
    pg = comp.getPortGroups()[0]
    assert isinstance(pg.getInnerGroupIRefs()[0], InnerPortGroupInCompositionInstanceRef)


def test_read_port_group_context_refs(parser):
    """CONTEXT-REF (multiple, ordered) is read into contextRefs preserving order and DEST."""
    comp = _comp()
    element = _pg(
        """
            <SHORT-NAME>PG</SHORT-NAME>
            <INNER-GROUP-IREFS>
                <INNER-GROUP-IREF>
                    <CONTEXT-REF DEST="SW-COMPONENT-PROTOTYPE">/Pkg/Comp/ProtoA</CONTEXT-REF>
                    <CONTEXT-REF DEST="SW-COMPONENT-PROTOTYPE">/Pkg/Comp/ProtoB</CONTEXT-REF>
                    <TARGET-REF DEST="PORT-GROUP">/Pkg/InnerGroup</TARGET-REF>
                </INNER-GROUP-IREF>
            </INNER-GROUP-IREFS>
        """
    )
    parser.readPortGroup(element, comp)
    pg = comp.getPortGroups()[0]
    iref = pg.getInnerGroupIRefs()[0]
    refs = iref.getContextRefs()
    assert len(refs) == 2
    assert refs[0].getValue() == "/Pkg/Comp/ProtoA"
    assert refs[0].getDest() == "SW-COMPONENT-PROTOTYPE"
    assert refs[1].getValue() == "/Pkg/Comp/ProtoB"
    assert iref.getTargetRef().getValue() == "/Pkg/InnerGroup"
