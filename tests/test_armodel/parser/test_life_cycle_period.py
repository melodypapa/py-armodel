"""Reader tests for the LifeCyclePeriod helper (LIFE-CYCLE-PERIOD: DATE + AR-RELEASE-VERSION + PRODUCT-RELEASE)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RevisionLabelString
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _parent_with(inner_xml: str) -> ET.Element:
    return ET.fromstring(f"<PARENT xmlns='{NS}'>{inner_xml}</PARENT>")


class TestGetLifeCyclePeriod:
    def test_read_all_fields(self, parser):
        """Test that DATE, AR-RELEASE-VERSION and PRODUCT-RELEASE are read with their spec types."""
        parent = _parent_with("<PERIOD-BEGIN>" "<DATE>2023-06-15T12:00:00+01:00</DATE>" "<AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION>" "<PRODUCT-RELEASE>1.2.3</PRODUCT-RELEASE>" "</PERIOD-BEGIN>")
        period = parser.getLifeCyclePeriod(parent, "PERIOD-BEGIN")
        assert period is not None
        assert isinstance(period.getDate(), DateTime)
        assert period.getDate().getValue() == "2023-06-15T12:00:00+01:00"
        assert isinstance(period.getArReleaseVersion(), RevisionLabelString)
        assert period.getArReleaseVersion().getValue() == "4.3.1"
        assert isinstance(period.getProductRelease(), RevisionLabelString)
        assert period.getProductRelease().getValue() == "1.2.3"

    def test_read_partial_fields(self, parser):
        """Test that absent DATE and PRODUCT-RELEASE elements leave the fields None."""
        parent = _parent_with("<PERIOD-BEGIN><AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION></PERIOD-BEGIN>")
        period = parser.getLifeCyclePeriod(parent, "PERIOD-BEGIN")
        assert period is not None
        assert period.getArReleaseVersion().getValue() == "4.3.1"
        assert period.getDate() is None
        assert period.getProductRelease() is None

    def test_read_absent_element(self, parser):
        """Test that a missing wrapper element yields None."""
        parent = _parent_with("")
        assert parser.getLifeCyclePeriod(parent, "PERIOD-BEGIN") is None
