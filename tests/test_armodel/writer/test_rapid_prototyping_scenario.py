"""Writer round-trip tests for RapidPrototypingScenario (Swc TPS Table 14.1, p.846).

writeRapidPrototypingScenario emits the RAPID-PROTOTYPING-SCENARIO group
(AUTOSAR_00052.xsd l.95550) in sequenceOffset order — HOST-SYSTEM-REF,
RPT-CONTAINERS, RPT-PROFILES, RPT-SYSTEM-REF — each wrapper element only when
non-empty, and calls writeIdentifiable exactly once for the inherited
Identifiable level (Rule 0025). NOT VP-capable (Rule 0020: the group declares
no VARIATION-POINT). Aggregated by ARPackage.element — the dispatch branch in
writeARPackageElement and the createRapidPrototypingScenario factory are
covered here too.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptEnablerImplTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RapidPrototypingScenario, RptHook
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "HOST-SYSTEM-REF",
    "RPT-CONTAINERS",
    "RPT-PROFILES",
    "RPT-SYSTEM-REF",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _full_scenario():
    scenario = RapidPrototypingScenario(AUTOSAR.getInstance(), "Scenario1")
    scenario.setUuid(String().setValue("5340cafe-beef-4f0e-9e5a-000000000003"))
    fragment = ShortNameFragment()
    fragment.setFragment(Identifier().setValue("Scenario1"))
    scenario.addShortNameFragment(fragment)

    scenario.setHostSystemRef(_ref("SYSTEM", "/System/HostSystem"))

    container = scenario.createRptContainer("Top1")
    hook = RptHook()
    hook.setCodeLabel(CIdentifier().setValue("RptHookFunc"))
    container.setRptHook(hook)

    profile = scenario.createRptProfile("Profile1")
    profile.setMaxServicePointId(PositiveInteger().setValue("10"))
    profile.setMinServicePointId(PositiveInteger().setValue("1"))
    profile.setStimEnabler(RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM))

    scenario.setRptSystemRef(_ref("SYSTEM", "/System/RptSystem"))
    return scenario


def _write_scenario(scenario):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeRapidPrototypingScenario(parent, scenario)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteRapidPrototypingScenario:
    def test_entry_point_emits_group_in_xsd_order_exactly_once(self):
        parent = _write_scenario(_full_scenario())
        scenario_element = parent.find("RAPID-PROTOTYPING-SCENARIO")

        own_tags = [child.tag for child in scenario_element if child.tag in XSD_ORDER]
        assert own_tags == XSD_ORDER

        direct_tags = [child.tag for child in scenario_element]
        for tag in XSD_ORDER:
            assert direct_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_scenario(_full_scenario())
        scenario_element = parent.find("RAPID-PROTOTYPING-SCENARIO")

        host_ref = scenario_element.find("HOST-SYSTEM-REF")
        assert host_ref.text == "/System/HostSystem"
        assert host_ref.attrib["DEST"] == "SYSTEM"

        containers = scenario_element.findall("RPT-CONTAINERS/RPT-CONTAINER")
        assert len(containers) == 1
        assert containers[0].find("SHORT-NAME").text == "Top1"
        assert containers[0].find("RPT-HOOKS/RPT-HOOK/CODE-LABEL").text == "RptHookFunc"

        profiles = scenario_element.findall("RPT-PROFILES/RPT-PROFILE")
        assert len(profiles) == 1
        assert profiles[0].find("SHORT-NAME").text == "Profile1"
        assert profiles[0].find("MAX-SERVICE-POINT-ID").text == "10"
        assert profiles[0].find("MIN-SERVICE-POINT-ID").text == "1"
        assert profiles[0].find("STIM-ENABLER").text == "RPT-ENABLER-RAM"

        rpt_ref = scenario_element.find("RPT-SYSTEM-REF")
        assert rpt_ref.text == "/System/RptSystem"
        assert rpt_ref.attrib["DEST"] == "SYSTEM"

    def test_entry_point_writes_identifiable_attributes(self):
        """UUID and SHORT-NAME-FRAGMENTS (Identifiable level) emitted via the writeIdentifiable base helper (Rule 0025)."""
        parent = _write_scenario(_full_scenario())
        scenario_element = parent.find("RAPID-PROTOTYPING-SCENARIO")

        assert scenario_element.attrib.get("UUID") == "5340cafe-beef-4f0e-9e5a-000000000003"
        assert scenario_element.find("SHORT-NAME-FRAGMENTS/SHORT-NAME-FRAGMENT/FRAGMENT").text == "Scenario1"

    def test_none_scenario_emits_nothing(self):
        parent = _write_scenario(None)

        assert len(parent) == 0

    def test_empty_scenario_emits_no_optional_wrappers(self):
        parent = _write_scenario(RapidPrototypingScenario(AUTOSAR.getInstance(), "Scenario1"))
        scenario_element = parent.find("RAPID-PROTOTYPING-SCENARIO")

        for tag in XSD_ORDER:
            assert scenario_element.find(tag) is None, tag

    def test_round_trip_full_through_rapid_prototyping_scenario(self):
        parent = _write_scenario(_full_scenario())
        reloaded = RapidPrototypingScenario(None, "Scenario1")
        ARXMLParser().readRapidPrototypingScenario(_namespaced_first_child(parent), reloaded)

        assert reloaded.getHostSystemRef().getValue() == "/System/HostSystem"
        assert reloaded.getHostSystemRef().getDest() == "SYSTEM"

        containers = reloaded.getRptContainers()
        assert len(containers) == 1
        assert containers[0].getShortName() == "Top1"
        assert containers[0].getRptHook().getCodeLabel().getValue() == "RptHookFunc"

        profiles = reloaded.getRptProfiles()
        assert len(profiles) == 1
        assert profiles[0].getShortName() == "Profile1"
        assert profiles[0].getMaxServicePointId().getValue() == 10
        assert profiles[0].getMinServicePointId().getValue() == 1
        assert profiles[0].getStimEnabler().getValue() == "RPT-ENABLER-RAM"

        assert reloaded.getRptSystemRef().getValue() == "/System/RptSystem"

    def test_round_trip_empty_through_rapid_prototyping_scenario(self):
        parent = _write_scenario(RapidPrototypingScenario(AUTOSAR.getInstance(), "Scenario1"))
        reloaded = RapidPrototypingScenario(None, "Scenario1")
        ARXMLParser().readRapidPrototypingScenario(_namespaced_first_child(parent), reloaded)

        assert reloaded.getHostSystemRef() is None
        assert reloaded.getRptContainers() == []
        assert reloaded.getRptProfiles() == []
        assert reloaded.getRptSystemRef() is None

    def test_round_trip_full_through_ar_package(self):
        """Document-level round trip: create via the ARPackage factory, save, reload via the ELEMENTS dispatch (five-place dispatch, Rule 0001.7)."""
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        scenario = ar_root.createRapidPrototypingScenario("Scenario1")
        scenario.setHostSystemRef(_ref("SYSTEM", "/System/HostSystem"))
        scenario.createRptContainer("Top1")
        scenario.createRptProfile("Profile1").setStimEnabler(RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM))
        scenario.setRptSystemRef(_ref("SYSTEM", "/System/RptSystem"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            scenarios = document_2.getARPackages()[0].getRapidPrototypingScenarios()
            assert len(scenarios) == 1
            assert isinstance(scenarios[0], RapidPrototypingScenario)
            assert scenarios[0].getShortName() == "Scenario1"
            assert scenarios[0].getHostSystemRef().getValue() == "/System/HostSystem"
            assert scenarios[0].getRptContainers()[0].getShortName() == "Top1"
            assert scenarios[0].getRptProfiles()[0].getStimEnabler().getValue() == "RPT-ENABLER-RAM"
            assert scenarios[0].getRptSystemRef().getValue() == "/System/RptSystem"
        finally:
            os.remove(file_path)
