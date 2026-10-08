"""
Tests for reading DDS-CP-CONFIG elements — DdsCpConfig, Table 6.175 (p.526, R23-11).

The class is a top-level package element (Aggregated by: ARPackage.element), so the tests
exercise both the reusable helper readDdsCpConfig on a standalone subtree and the ARPackage
`element` polymorphic dispatch branch (tag DDS-CP-CONFIG inside an AR-PACKAGE) — the
IPv6ExtHeaderFilterSet five-place pattern (XSD complexType DDS-CP-CONFIG,
AUTOSAR_00052.xsd l.28589; group DDS-CP-CONFIG l.28557: DDS-DOMAINS, DDS-QOS-PROFILES).

ddsQosProfile children are read via the synced readDdsCpQosProfile (real coverage);
ddsDomain children via the synced readDdsCpDomain (real coverage).

Round-trip counterpart: tests/test_armodel/writer/test_writer_dds_cp_config.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpDomain, DdsCpQosProfile
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpConfig

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<DDS-CP-CONFIG xmlns='{NS}'>{inner}</DDS-CP-CONFIG>")


class TestReadDdsCpConfig:
    """Tests for readDdsCpConfig — own group field values (Table 6.175)."""

    def _read(self, parser, inner):
        config = DdsCpConfig(AUTOSAR.getInstance(), "DdsCpConfig1")
        parser.readDdsCpConfig(_snip(inner), config)
        return config

    def test_read_sets_all_fields(self, parser):
        """Test that domains and QOS profiles are read with their values."""
        config = self._read(
            parser,
            "<DDS-DOMAINS>"
            "<DDS-CP-DOMAIN><SHORT-NAME>Domain1</SHORT-NAME><DOMAIN-ID>1</DOMAIN-ID></DDS-CP-DOMAIN>"
            "</DDS-DOMAINS>"
            "<DDS-QOS-PROFILES>"
            "<DDS-CP-QOS-PROFILE><SHORT-NAME>Profile1</SHORT-NAME><RELIABILITY><RELIABILITY-KIND>RELIABLE</RELIABILITY-KIND></RELIABILITY></DDS-CP-QOS-PROFILE>"
            "</DDS-QOS-PROFILES>",
        )
        domains = config.getDdsDomains()
        assert len(domains) == 1
        assert isinstance(domains[0], DdsCpDomain)
        assert domains[0].getShortName() == "Domain1"
        assert domains[0].getDomainId().getValue() == 1
        profiles = config.getDdsQosProfiles()
        assert len(profiles) == 1
        assert isinstance(profiles[0], DdsCpQosProfile)
        assert profiles[0].getShortName() == "Profile1"
        assert profiles[0].getReliability() is not None
        assert profiles[0].getReliability().getReliabilityKind().getValue() == "RELIABLE"

    def test_read_empty(self, parser):
        """Test that absent wrappers leave the fields empty."""
        config = self._read(parser, "")
        assert config.getDdsDomains() == []
        assert config.getDdsQosProfiles() == []


class TestReadDdsCpConfigDispatch:
    """Tests for the ARPackage.element polymorphic dispatch (tag DDS-CP-CONFIG)."""

    def test_dispatch_creates_and_populates_config(self, parser):
        """Test that a DDS-CP-CONFIG element inside ELEMENTS dispatches to readDdsCpConfig."""
        package = AUTOSAR.getInstance().createARPackage("DdsCpConfigs")
        root = _snip(
            "<ELEMENTS>"
            "<DDS-CP-CONFIG><SHORT-NAME>DdsCpConfig1</SHORT-NAME>"
            "<DDS-DOMAINS><DDS-CP-DOMAIN><SHORT-NAME>Domain1</SHORT-NAME></DDS-CP-DOMAIN></DDS-DOMAINS>"
            "</DDS-CP-CONFIG>"
            "</ELEMENTS>"
        )
        parser.readARPackageElements(root, package)
        config = package.getReferrableElement("DdsCpConfig1", DdsCpConfig)
        assert isinstance(config, DdsCpConfig)
        assert len(config.getDdsDomains()) == 1
        assert config.getDdsDomains()[0].getShortName() == "Domain1"
