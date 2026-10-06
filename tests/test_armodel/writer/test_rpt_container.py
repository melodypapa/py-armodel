"""Writer round-trip tests for RptContainer (Swc TPS Table 14.2, p.847).

writeRptContainer emits the RPT-CONTAINER group (AUTOSAR_00052.xsd l.99633) in
sequenceOffset order — BY-PASS-POINT-IREFS, EXPLICIT-RPT-PROFILE-SELECTION-REFS,
RPT-CONTAINERS (recursive sub-containers), RPT-EXECUTABLE-ENTITY-PROPERTIES,
RPT-HOOKS, RPT-IMPL-POLICY, RPT-SW-PROTOTYPING-ACCESS, VARIATION-POINT last
(sequenceOffset 10000, Applicable for RptContainer.rptContainer, Rule 0020) —
each wrapper element only when non-empty, and calls writeIdentifiable exactly
once for the inherited Identifiable level (Rule 0025). rptHook keeps the PDF
multiplicity 0..1 (Rule 0015: the PDF/markdown table wins) even though the XSD
renders the RPT-HOOKS role as an unbounded wrapper ("upper multiplicity
increased to * due to resolving an atpVariation stereotype"), so the wrapper
holds exactly one RPT-HOOK item. The RapidPrototypingScenario.rptContainer
dispatch is that class's own queued sync, so the helper is exercised directly.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptAccessEnum, RptPreparationEnum, RptSwPrototypingAccess
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptContainer, RptExecutableEntityProperties, RptHook, RptImplPolicy
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "BY-PASS-POINT-IREFS",
    "EXPLICIT-RPT-PROFILE-SELECTION-REFS",
    "RPT-CONTAINERS",
    "RPT-EXECUTABLE-ENTITY-PROPERTIES",
    "RPT-HOOKS",
    "RPT-IMPL-POLICY",
    "RPT-SW-PROTOTYPING-ACCESS",
    "VARIATION-POINT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _full_container():
    container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
    container.setUuid(String().setValue("5340cafe-beef-4f0e-9e5a-000000000002"))
    fragment = ShortNameFragment()
    fragment.setFragment(Identifier().setValue("RptContainer1"))
    container.addShortNameFragment(fragment)

    iref1 = AnyInstanceRef()
    iref1.addContextElementRef(RefType().setValue("/comp/Swc1/Data1"))
    iref1.setTargetRef(RefType().setValue("/comp/Swc1/Data2"))
    container.addByPassPointIRef(iref1)
    iref2 = AnyInstanceRef()
    iref2.setTargetRef(RefType().setValue("/comp/Swc1/Data3"))
    container.addByPassPointIRef(iref2)

    ref1 = RefType()
    ref1.setValue("/RptScenario/RptProfile1")
    ref1.setDest("RPT-PROFILE")
    container.addExplicitRptProfileSelectionRef(ref1)
    container.addExplicitRptProfileSelectionRef(RefType().setValue("/RptScenario/RptProfile2"))

    sub_container = container.createRptContainer("Sub1")
    sub_iref = AnyInstanceRef()
    sub_iref.setTargetRef(RefType().setValue("/comp/Swc1/SubData"))
    sub_container.addByPassPointIRef(sub_iref)

    properties = RptExecutableEntityProperties()
    properties.setMaxRptEventId(PositiveInteger().setValue("100"))
    properties.setMinRptEventId(PositiveInteger().setValue("1"))
    container.setRptExecutableEntityProperties(properties)

    hook = RptHook()
    hook.setCodeLabel(CIdentifier().setValue("RptHookFunc"))
    container.setRptHook(hook)

    policy = RptImplPolicy()
    policy.setRptPreparationLevel(RptPreparationEnum().setValue(RptPreparationEnum.RPT_LEVEL_2))
    container.setRptImplPolicy(policy)

    access = RptSwPrototypingAccess()
    access.setRptReadAccess(RptAccessEnum().setValue(RptAccessEnum.PROTECTED))
    container.setRptSwPrototypingAccess(access)

    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue("VP1"))
    container.setVariationPoint(vp)
    return container


def _write_rpt_container(container):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeRptContainer(parent, container)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteRptContainer:
    def test_entry_point_emits_group_in_xsd_order_exactly_once(self):
        parent = _write_rpt_container(_full_container())
        container_element = parent.find("RPT-CONTAINER")

        own_tags = [child.tag for child in container_element if child.tag in XSD_ORDER]
        assert own_tags == XSD_ORDER

        # exactly once per instance — direct children only (the recursive
        # RPT-CONTAINERS sub-container legitimately repeats the group tags)
        direct_tags = [child.tag for child in container_element]
        for tag in XSD_ORDER:
            assert direct_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_rpt_container(_full_container())
        container_element = parent.find("RPT-CONTAINER")

        assert container_element.find("BY-PASS-POINT-IREFS/BY-PASS-POINT-IREF/CONTEXT-ELEMENT-REF").text == "/comp/Swc1/Data1"
        assert container_element.find("BY-PASS-POINT-IREFS/BY-PASS-POINT-IREF/TARGET-REF").text == "/comp/Swc1/Data2"
        assert len(container_element.findall("BY-PASS-POINT-IREFS/BY-PASS-POINT-IREF")) == 2

        refs = container_element.findall("EXPLICIT-RPT-PROFILE-SELECTION-REFS/EXPLICIT-RPT-PROFILE-SELECTION-REF")
        assert len(refs) == 2
        assert refs[0].text == "/RptScenario/RptProfile1"
        assert refs[0].attrib["DEST"] == "RPT-PROFILE"
        assert refs[1].text == "/RptScenario/RptProfile2"

        assert container_element.find("RPT-CONTAINERS/RPT-CONTAINER/SHORT-NAME").text == "Sub1"

        assert container_element.find("RPT-EXECUTABLE-ENTITY-PROPERTIES/MAX-RPT-EVENT-ID").text == "100"
        assert container_element.find("RPT-EXECUTABLE-ENTITY-PROPERTIES/MIN-RPT-EVENT-ID").text == "1"

        hooks_element = container_element.find("RPT-HOOKS")
        assert len(hooks_element) == 1  # PDF Mult 0..1 (Rule 0015) — one item despite the XSD unbounded wrapper
        assert hooks_element.find("RPT-HOOK/CODE-LABEL").text == "RptHookFunc"

        assert container_element.find("RPT-IMPL-POLICY/RPT-PREPARATION-LEVEL").text == "RPT-LEVEL-2"
        assert container_element.find("RPT-SW-PROTOTYPING-ACCESS/RPT-READ-ACCESS").text == "PROTECTED"
        assert container_element.find("VARIATION-POINT") is not None

    def test_entry_point_writes_identifiable_attributes(self):
        """UUID and SHORT-NAME-FRAGMENTS (Identifiable level) emitted via the writeIdentifiable base helper (Rule 0025)."""
        parent = _write_rpt_container(_full_container())
        container_element = parent.find("RPT-CONTAINER")

        assert container_element.attrib.get("UUID") == "5340cafe-beef-4f0e-9e5a-000000000002"
        assert container_element.find("SHORT-NAME-FRAGMENTS/SHORT-NAME-FRAGMENT/FRAGMENT").text == "RptContainer1"

    def test_none_container_emits_nothing(self):
        parent = _write_rpt_container(None)

        assert len(parent) == 0

    def test_empty_container_emits_no_optional_wrappers(self):
        parent = _write_rpt_container(RptContainer(AUTOSAR.getInstance(), "RptContainer1"))
        container_element = parent.find("RPT-CONTAINER")

        for tag in XSD_ORDER:
            assert container_element.find(tag) is None, tag

    def test_round_trip_full_through_rpt_container(self):
        parent = _write_rpt_container(_full_container())
        reloaded = RptContainer(None, "RptContainer1")
        ARXMLParser().readRptContainer(_namespaced_first_child(parent), reloaded)

        irefs = reloaded.getByPassPointIRefs()
        assert len(irefs) == 2
        assert [ref.getValue() for ref in irefs[0].getContextElementRefs()] == ["/comp/Swc1/Data1"]
        assert irefs[0].getTargetRef().getValue() == "/comp/Swc1/Data2"
        assert irefs[1].getTargetRef().getValue() == "/comp/Swc1/Data3"

        refs = reloaded.getExplicitRptProfileSelectionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/RptScenario/RptProfile1"
        assert refs[0].getDest() == "RPT-PROFILE"
        assert refs[1].getValue() == "/RptScenario/RptProfile2"

        sub_containers = reloaded.getRptContainers()
        assert len(sub_containers) == 1
        assert sub_containers[0].getShortName() == "Sub1"
        sub_irefs = sub_containers[0].getByPassPointIRefs()
        assert len(sub_irefs) == 1
        assert sub_irefs[0].getTargetRef().getValue() == "/comp/Swc1/SubData"

        assert reloaded.getRptExecutableEntityProperties().getMaxRptEventId().getValue() == 100
        assert reloaded.getRptHook().getCodeLabel().getValue() == "RptHookFunc"
        assert reloaded.getRptImplPolicy().getRptPreparationLevel().getValue() == "RPT-LEVEL-2"
        assert reloaded.getRptSwPrototypingAccess().getRptReadAccess().getValue() == "PROTECTED"
        assert reloaded.getVariationPoint() is not None

    def test_round_trip_empty_through_rpt_container(self):
        parent = _write_rpt_container(RptContainer(AUTOSAR.getInstance(), "RptContainer1"))
        reloaded = RptContainer(None, "RptContainer1")
        ARXMLParser().readRptContainer(_namespaced_first_child(parent), reloaded)

        assert reloaded.getByPassPointIRefs() == []
        assert reloaded.getExplicitRptProfileSelectionRefs() == []
        assert reloaded.getRptContainers() == []
        assert reloaded.getRptExecutableEntityProperties() is None
        assert reloaded.getRptHook() is None
        assert reloaded.getRptImplPolicy() is None
        assert reloaded.getRptSwPrototypingAccess() is None
        assert reloaded.getVariationPoint() is None
