"""Tests for the readPrivacyLevel handler (R23-11 PrivacyLevel, Table 3.4, p.18)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import PrivacyLevel
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadPrivacyLevel:
    """Tests for readPrivacyLevel handler (R23-11 PrivacyLevel, Table 3.4, p.18)."""

    def test_read_privacy_level_full(self, parser):
        element = _snip(
            """
                <COMPU-METHOD-REF DEST="COMPU-METHOD">/LogAndTrace/CompuMethods/PrivacyLevels</COMPU-METHOD-REF>
                <PRIVACY-LEVEL>1</PRIVACY-LEVEL>
            """,
            root_tag="PRIVACY-LEVEL",
        )
        privacy_level = PrivacyLevel()
        parser.readPrivacyLevel(element, privacy_level)
        assert privacy_level.getCompuMethodRef().getValue() == "/LogAndTrace/CompuMethods/PrivacyLevels"
        assert privacy_level.getCompuMethodRef().getDest() == "COMPU-METHOD"
        assert privacy_level.getPrivacyLevel().getValue() == 1

    def test_read_privacy_level_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="PRIVACY-LEVEL",
        )
        privacy_level = PrivacyLevel()
        parser.readPrivacyLevel(element, privacy_level)
        assert privacy_level.getCompuMethodRef() is None
        assert privacy_level.getPrivacyLevel() is None
