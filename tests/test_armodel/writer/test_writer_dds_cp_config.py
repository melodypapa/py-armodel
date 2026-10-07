"""
Writer tests for DDS-CP-CONFIG elements — DdsCpConfig, Table 6.175 (p.526, R23-11).

writeDdsCpConfig creates the DDS-CP-CONFIG element, emits the IDENTIFIABLE level
(SHORT-NAME, UUID — writeIdentifiable, called exactly once, Rule 0013.1/0025), then its own
group members in XSD sequenceOffset order (group DDS-CP-CONFIG, AUTOSAR_00052.xsd l.28557):
DDS-DOMAINS, DDS-QOS-PROFILES. Wrapper elements are emitted only when non-empty. Both child
kinds are serialized via their synced helpers writeDdsCpDomain / writeDdsCpQosProfile (real
coverage). The ARPackage `element` polymorphic dispatch branch is covered too.

Round-trip counterpart: tests/test_armodel/parser/test_dds_cp_config.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsTopicData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpQosProfile
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpConfig
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_config() -> DdsCpConfig:
    config = DdsCpConfig(AUTOSAR.getInstance(), "DdsCpConfig1")
    domain = config.createDdsDomain("Domain1")
    domain.setDomainId(PositiveInteger().setValue("1"))
    profile = config.createDdsQosProfile("Profile1")
    profile.setTopicData(DdsTopicData().setTopicData(String().setValue("SomeData")))
    return config


class TestWriteDdsCpConfig:
    def test_write_emits_members_in_xsd_order(self):
        """Test that the writer emits SHORT-NAME, DDS-DOMAINS then DDS-QOS-PROFILES with child values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConfig(parent, _new_config())

        child = parent.find("DDS-CP-CONFIG")
        assert child is not None
        children = [c.tag for c in child]
        assert children[0] == "SHORT-NAME"
        assert child.find("SHORT-NAME").text == "DdsCpConfig1"
        assert children.index("DDS-DOMAINS") < children.index("DDS-QOS-PROFILES")
        assert child.find("DDS-DOMAINS/DDS-CP-DOMAIN/SHORT-NAME").text == "Domain1"
        assert child.find("DDS-DOMAINS/DDS-CP-DOMAIN/DOMAIN-ID").text == "1"
        assert child.find("DDS-QOS-PROFILES/DDS-CP-QOS-PROFILE/SHORT-NAME").text == "Profile1"
        assert child.find("DDS-QOS-PROFILES/DDS-CP-QOS-PROFILE/TOPIC-DATA/TOPIC-DATA").text == "SomeData"

    def test_write_empty_omits_members(self):
        """Test that an empty config emits only the SHORT-NAME (wrapper lists omitted when empty)."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConfig(parent, DdsCpConfig(AUTOSAR.getInstance(), "Empty"))
        child = parent.find("DDS-CP-CONFIG")
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_dispatches_on_package_element(self):
        """Test the ARPackage.element polymorphic writer dispatch (isinstance branch)."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DdsCpConfigs")
        package.createDdsConfig("DdsCpConfig1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)
        node = parent.find("ELEMENTS/DDS-CP-CONFIG")
        assert node is not None
        assert node.find("SHORT-NAME").text == "DdsCpConfig1"

    def test_round_trip_via_file(self, tmp_path):
        """Element-level round-trip: write, reload, read back via readDdsCpConfig, assert field values."""
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDdsCpConfig(parent, _new_config())
        inner = ET.tostring(parent[0]).decode("utf-8")

        out_file = str(tmp_path / "dds_cp_config.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

        AUTOSAR.getInstance().new()
        re_document = AUTOSAR.getInstance()
        re_document.setARRelease("R23-11")
        parser = ARXMLParser(options={"warning": True})
        re_config = DdsCpConfig(re_document, "DdsCpConfig1")
        parser.readDdsCpConfig(ET.parse(out_file).getroot()[0], re_config)

        assert re_config.getShortName() == "DdsCpConfig1"
        domains = re_config.getDdsDomains()
        assert len(domains) == 1
        assert domains[0].getShortName() == "Domain1"
        assert domains[0].getDomainId().getValue() == 1
        profiles = re_config.getDdsQosProfiles()
        assert len(profiles) == 1
        assert isinstance(profiles[0], DdsCpQosProfile)
        assert profiles[0].getTopicData().getTopicData().getValue() == "SomeData"
