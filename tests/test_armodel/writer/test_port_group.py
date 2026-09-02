"""Writer round-trip tests for PortGroup (value-level, R23-11 Table 4.94)."""

import os
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    comp = pkg.createCompositionSwComponentType("Comp")
    pg = comp.createPortGroup("PG")

    iref = InnerPortGroupInCompositionInstanceRef()
    tref = RefType()
    tref.setValue("/Pkg/InnerGroup")
    tref.setDest("PORT-GROUP")
    iref.setTargetRef(tref)
    pg.addInnerGroupIRef(iref)

    oref = RefType()
    oref.setValue("/Pkg/OuterPort")
    oref.setDest("PORT-PROTOTYPE")
    pg.addOuterPortRef(oref)
    return document


def _reload(path):
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser = ARXMLParser()
    parser.load(path, document)
    return document


def test_port_group_round_trip(tmp_path):
    """PortGroup inner-group-iref and outer-port-ref values survive a write -> reload round-trip."""
    document = _build()
    path = os.path.join(str(tmp_path), "pg.arxml")
    ARXMLWriter().save(path, document)

    reloaded = _reload(path)
    comp = reloaded.find("/Pkg/Comp")
    pg = comp.getPortGroups()[0]
    assert pg.getShortName() == "PG"
    assert len(pg.getInnerGroupIRefs()) == 1
    assert pg.getInnerGroupIRefs()[0].getTargetRef().getValue() == "/Pkg/InnerGroup"
    assert len(pg.getOuterPortRefs()) == 1
    assert pg.getOuterPortRefs()[0].getValue() == "/Pkg/OuterPort"


def test_port_group_empty_wrapper_round_trip(tmp_path):
    """A PortGroup with no inner/outer members round-trips to empty lists (no silent drop)."""
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    pkg.createCompositionSwComponentType("Comp").createPortGroup("PG")

    path = os.path.join(str(tmp_path), "pg_empty.arxml")
    ARXMLWriter().save(path, document)

    reloaded = _reload(path)
    comp = reloaded.find("/Pkg/Comp")
    pg = comp.getPortGroups()[0]
    assert pg.getInnerGroupIRefs() == []
    assert pg.getOuterPortRefs() == []


def test_port_group_context_refs_round_trip(tmp_path):
    """CONTEXT-REF (ordered) survives write -> reload with correct DEST, order, and TARGET-REF."""
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Pkg")
    comp = pkg.createCompositionSwComponentType("Comp")
    pg = comp.createPortGroup("PG")

    iref = InnerPortGroupInCompositionInstanceRef()
    c1 = RefType()
    c1.setValue("/Pkg/Comp/ProtoA")
    c1.setDest("SW-COMPONENT-PROTOTYPE")
    c2 = RefType()
    c2.setValue("/Pkg/Comp/ProtoB")
    c2.setDest("SW-COMPONENT-PROTOTYPE")
    iref.addContextRef(c1).addContextRef(c2)
    tref = RefType()
    tref.setValue("/Pkg/InnerGroup")
    tref.setDest("PORT-GROUP")
    iref.setTargetRef(tref)
    pg.addInnerGroupIRef(iref)

    path = os.path.join(str(tmp_path), "pg_ctx.arxml")
    ARXMLWriter().save(path, document)

    # CONTEXT-REF must be written before TARGET-REF (xml.sequenceOffset 20 < 30)
    raw = ET.parse(path).getroot()
    ns = "{http://autosar.org/schema/r4.0}"
    ig = raw.find(".//%sINNER-GROUP-IREF" % ns)
    tags = [child.tag.replace(ns, "") for child in list(ig)]
    assert tags.index("CONTEXT-REF") < tags.index("TARGET-REF")

    reloaded = _reload(path)
    comp_r = reloaded.find("/Pkg/Comp")
    pg_r = comp_r.getPortGroups()[0]
    iref_r = pg_r.getInnerGroupIRefs()[0]
    refs = iref_r.getContextRefs()
    assert len(refs) == 2
    assert refs[0].getValue() == "/Pkg/Comp/ProtoA"
    assert refs[0].getDest() == "SW-COMPONENT-PROTOTYPE"
    assert refs[1].getValue() == "/Pkg/Comp/ProtoB"
    assert iref_r.getTargetRef().getValue() == "/Pkg/InnerGroup"
