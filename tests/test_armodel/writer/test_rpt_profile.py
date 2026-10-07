"""Writer round-trip tests for RptProfile (Swc TPS Table 14.7, p.854).

writeRptProfile emits the RPT-PROFILE group (AUTOSAR_00052.xsd l.100138) in
sequenceOffset order — MAX-SERVICE-POINT-ID, MIN-SERVICE-POINT-ID,
SERVICE-POINT-SYMBOL-POST, SERVICE-POINT-SYMBOL-PRE, STIM-ENABLER — and calls
writeIdentifiable exactly once for the inherited Identifiable level
(SHORT-NAME, UUID attribute, CATEGORY, ..., Rule 0025). RptProfile is
aggregated by RapidPrototypingScenario.rptProfile; the
RapidPrototypingScenario dispatch is that class's own queued sync, so the
helper is exercised directly.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptEnablerImplTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptProfile
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = [
    "MAX-SERVICE-POINT-ID",
    "MIN-SERVICE-POINT-ID",
    "SERVICE-POINT-SYMBOL-POST",
    "SERVICE-POINT-SYMBOL-PRE",
    "STIM-ENABLER",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _full_profile():
    profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")
    profile.setUuid(String().setValue("5340cafe-beef-4f0e-9e5a-000000000001"))
    fragment = ShortNameFragment()
    fragment.setFragment(Identifier().setValue("RptProfile1"))
    profile.addShortNameFragment(fragment)
    profile.setMaxServicePointId(PositiveInteger().setValue("4"))
    profile.setMinServicePointId(PositiveInteger().setValue("2"))
    profile.setServicePointSymbolPost(CIdentifier().setValue("Rpt_PostServicePoint"))
    profile.setServicePointSymbolPre(CIdentifier().setValue("Rpt_PreServicePoint"))
    profile.setStimEnabler(RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM))
    return profile


def _write_rpt_profile(profile):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeRptProfile(parent, profile)
    return parent


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteRptProfile:
    def test_entry_point_emits_group_in_xsd_order_exactly_once(self):
        parent = _write_rpt_profile(_full_profile())
        profile_element = parent.find("RPT-PROFILE")

        own_tags = [child.tag for child in profile_element if child.tag in XSD_ORDER]
        assert own_tags == XSD_ORDER

        all_tags = [child.tag for child in profile_element.iter()]
        for tag in XSD_ORDER:
            assert all_tags.count(tag) == 1, tag

    def test_entry_point_writes_field_values(self):
        parent = _write_rpt_profile(_full_profile())
        profile_element = parent.find("RPT-PROFILE")

        assert profile_element.find("MAX-SERVICE-POINT-ID").text == "4"
        assert profile_element.find("MIN-SERVICE-POINT-ID").text == "2"
        assert profile_element.find("SERVICE-POINT-SYMBOL-POST").text == "Rpt_PostServicePoint"
        assert profile_element.find("SERVICE-POINT-SYMBOL-PRE").text == "Rpt_PreServicePoint"
        assert profile_element.find("STIM-ENABLER").text == "RPT-ENABLER-RAM"

    def test_entry_point_writes_identifiable_attributes(self):
        """SHORT-NAME, SHORT-NAME-FRAGMENTS and UUID (Identifiable level) emitted via the writeIdentifiable base helper (Rule 0025)."""
        parent = _write_rpt_profile(_full_profile())
        profile_element = parent.find("RPT-PROFILE")

        assert profile_element.attrib.get("UUID") == "5340cafe-beef-4f0e-9e5a-000000000001"
        assert profile_element.find("SHORT-NAME-FRAGMENTS/SHORT-NAME-FRAGMENT/FRAGMENT").text == "RptProfile1"

    def test_none_profile_emits_nothing(self):
        parent = _write_rpt_profile(None)

        assert len(parent) == 0

    def test_empty_profile_emits_no_optional_elements(self):
        parent = _write_rpt_profile(RptProfile(AUTOSAR.getInstance(), "RptProfile1"))
        profile_element = parent.find("RPT-PROFILE")

        for tag in XSD_ORDER:
            assert profile_element.find(tag) is None, tag

    def test_round_trip_full_through_rpt_profile(self):
        parent = _write_rpt_profile(_full_profile())
        reloaded = RptProfile(None, "RptProfile1")
        ARXMLParser().readRptProfile(_namespaced_first_child(parent), reloaded)

        assert reloaded.getMaxServicePointId().getValue() == 4
        assert reloaded.getMinServicePointId().getValue() == 2
        assert reloaded.getServicePointSymbolPost().getValue() == "Rpt_PostServicePoint"
        assert reloaded.getServicePointSymbolPre().getValue() == "Rpt_PreServicePoint"
        assert reloaded.getStimEnabler().getValue() == "RPT-ENABLER-RAM"

    def test_round_trip_empty_through_rpt_profile(self):
        parent = _write_rpt_profile(RptProfile(AUTOSAR.getInstance(), "RptProfile1"))
        reloaded = RptProfile(None, "RptProfile1")
        ARXMLParser().readRptProfile(_namespaced_first_child(parent), reloaded)

        assert reloaded.getMaxServicePointId() is None
        assert reloaded.getMinServicePointId() is None
        assert reloaded.getServicePointSymbolPost() is None
        assert reloaded.getServicePointSymbolPre() is None
        assert reloaded.getStimEnabler() is None
