"""Writer round-trip tests for RptHook (Swc TPS Table 14.3, p.848).

writeRptHook emits the RPT-HOOK group (AUTOSAR_00052.xsd l.100040) in
sequenceOffset order — CODE-LABEL, MCD-IDENTIFIER, RPT-AR-HOOK-IREF (an
AnyInstanceRef iref), the SDGS wrapper only when non-empty (unbounded SDG),
VARIATION-POINT last (sequenceOffset 10000, Applicable for
RptContainer.rptHook, Rule 0020) — and calls writeARObject exactly once for
the inherited S/T attributes (Rule 0025). RptHook is aggregated by
RptContainer.rptHook; the RptContainer dispatch is that class's own queued
sync, so the helper is exercised directly.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, NameToken, RefType, String, VerbatimStringPlain
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptHook
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdg, SdgContents
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "CODE-LABEL",
    "MCD-IDENTIFIER",
    "RPT-AR-HOOK-IREF",
    "SDGS",
    "VARIATION-POINT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _full_hook():
    hook = RptHook()
    hook.setChecksum(String().setValue("1234"))
    hook.setCodeLabel(CIdentifier().setValue("RptHookFunc"))
    hook.setMcdIdentifier(NameToken().setValue("McdHook"))
    iref = AnyInstanceRef()
    iref.addContextElementRef(RefType().setValue("/comp/Swc1/Data1"))
    iref.setTargetRef(RefType().setValue("/comp/Swc1/Data2"))
    hook.setRptArHookIRef(iref)
    sdg = Sdg()
    sdg.setGID(NameToken().setValue("toolData"))
    contents = SdgContents()
    sd = Sd()
    sd.setGID(NameToken().setValue("key1"))
    sd.setValue(VerbatimStringPlain().setValue("value1"))
    contents.addSd(sd)
    sdg.setSdgContentsType(contents)
    hook.addSdg(sdg)
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue("VP1"))
    hook.setVariationPoint(vp)
    return hook


def _write_rpt_hook(hook):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeRptHook(parent, hook)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteRptHook:
    def test_entry_point_emits_group_in_xsd_order_exactly_once(self):
        parent = _write_rpt_hook(_full_hook())
        hook_element = parent.find("RPT-HOOK")

        assert [child.tag for child in hook_element] == XSD_ORDER

        all_tags = [child.tag for child in hook_element.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_rpt_hook(_full_hook())
        hook_element = parent.find("RPT-HOOK")

        assert hook_element.find("CODE-LABEL").text == "RptHookFunc"
        assert hook_element.find("MCD-IDENTIFIER").text == "McdHook"
        assert hook_element.find("RPT-AR-HOOK-IREF/CONTEXT-ELEMENT-REF").text == "/comp/Swc1/Data1"
        assert hook_element.find("RPT-AR-HOOK-IREF/TARGET-REF").text == "/comp/Swc1/Data2"
        assert hook_element.find("SDGS/SDG").attrib["GID"] == "toolData"
        assert hook_element.find("SDGS/SDG/SD").attrib["GID"] == "key1"
        assert hook_element.find("SDGS/SDG/SD").text == "value1"
        assert hook_element.find("VARIATION-POINT") is not None

    def test_entry_point_writes_ar_object_attributes(self):
        """S/T (ARObject level) emitted via the writeARObject base helper (Rule 0025)."""
        parent = _write_rpt_hook(_full_hook())
        hook_element = parent.find("RPT-HOOK")

        assert hook_element.attrib.get("S") == "1234"

    def test_empty_hook_emits_no_optional_wrappers(self):
        parent = _write_rpt_hook(RptHook())
        hook_element = parent.find("RPT-HOOK")

        assert len(hook_element) == 0
        assert hook_element.find("SDGS") is None
        assert hook_element.find("VARIATION-POINT") is None

    def test_round_trip_full_through_rpt_hook(self):
        parent = _write_rpt_hook(_full_hook())
        reloaded = RptHook()
        ARXMLParser().readRptHook(_namespaced_first_child(parent), reloaded)

        assert reloaded.getCodeLabel().getValue() == "RptHookFunc"
        assert reloaded.getMcdIdentifier().getValue() == "McdHook"

        iref = reloaded.getRptArHookIRef()
        assert iref is not None
        assert [ref.getValue() for ref in iref.getContextElementRefs()] == ["/comp/Swc1/Data1"]
        assert iref.getTargetRef().getValue() == "/comp/Swc1/Data2"

        sdgs = reloaded.getSdgs()
        assert len(sdgs) == 1
        assert sdgs[0].getGID().getValue() == "toolData"
        assert sdgs[0].getSdgContentsType().getSds()[0].getValue().getValue() == "value1"

        assert reloaded.getVariationPoint() is not None

    def test_round_trip_empty_through_rpt_hook(self):
        parent = _write_rpt_hook(RptHook())
        reloaded = RptHook()
        ARXMLParser().readRptHook(_namespaced_first_child(parent), reloaded)

        assert reloaded.getCodeLabel() is None
        assert reloaded.getMcdIdentifier() is None
        assert reloaded.getRptArHookIRef() is None
        assert reloaded.getSdgs() == []
        assert reloaded.getVariationPoint() is None
