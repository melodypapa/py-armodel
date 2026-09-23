"""Reader tests for LifeCycleInfoSet (LIFE-CYCLE-INFO-SET per XSD group AUTOSAR_00052.xsd L76621: DEFAULT-LC-STATE-REF, DEFAULT-PERIOD-BEGIN, DEFAULT-PERIOD-END, LIFE-CYCLE-INFOS, USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF)."""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

_FULL_INNER = (
    '<DEFAULT-LC-STATE-REF DEST="LIFE-CYCLE-STATE">/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/valid</DEFAULT-LC-STATE-REF>'
    "<DEFAULT-PERIOD-BEGIN>"
    "<DATE>2023-01-01T00:00:00+01:00</DATE>"
    "<AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION>"
    "</DEFAULT-PERIOD-BEGIN>"
    "<DEFAULT-PERIOD-END>"
    "<DATE>2024-12-31T23:59:59+01:00</DATE>"
    "<PRODUCT-RELEASE>1.0.0</PRODUCT-RELEASE>"
    "</DEFAULT-PERIOD-END>"
    "<LIFE-CYCLE-INFOS>"
    '<LIFE-CYCLE-INFO><LC-OBJECT-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSts1</LC-OBJECT-REF></LIFE-CYCLE-INFO>'
    "</LIFE-CYCLE-INFOS>"
    '<USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF DEST="LIFE-CYCLE-STATE-DEFINITION-GROUP">/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates</USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF>'
)

_PERIODS_ONLY_INNER = (
    "<DEFAULT-PERIOD-BEGIN>"
    "<DATE>2023-01-01T00:00:00+01:00</DATE>"
    "</DEFAULT-PERIOD-BEGIN>"
    "<DEFAULT-PERIOD-END>"
    "<DATE>2024-12-31T23:59:59+01:00</DATE>"
    "<PRODUCT-RELEASE>1.0.0</PRODUCT-RELEASE>"
    "</DEFAULT-PERIOD-END>"
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _set_element(inner_xml: str) -> ET.Element:
    return ET.fromstring(f'<LIFE-CYCLE-INFO-SET xmlns="{NS}"><SHORT-NAME>lcis</SHORT-NAME>{inner_xml}</LIFE-CYCLE-INFO-SET>')


def _new_info_set() -> LifeCycleInfoSet:
    return LifeCycleInfoSet(parent=MagicMock(), short_name="lcis")


class TestReadLifeCycleInfoSet:
    def test_read_all_fields(self, parser):
        """Test that all five LIFE-CYCLE-INFO-SET children are read with their spec types and values."""
        info_set = _new_info_set()
        parser.readLifeCycleInfoSet(_set_element(_FULL_INNER), info_set)
        assert info_set.getDefaultLcStateRef().getValue() == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/valid"
        assert isinstance(info_set.getDefaultPeriodBegin(), LifeCyclePeriod)
        assert info_set.getDefaultPeriodBegin().getDate().getValue() == "2023-01-01T00:00:00+01:00"
        assert info_set.getDefaultPeriodBegin().getArReleaseVersion().getValue() == "4.3.1"
        assert isinstance(info_set.getDefaultPeriodEnd(), LifeCyclePeriod)
        assert info_set.getDefaultPeriodEnd().getDate().getValue() == "2024-12-31T23:59:59+01:00"
        assert info_set.getDefaultPeriodEnd().getProductRelease().getValue() == "1.0.0"
        infos = info_set.getLifeCycleInfos()
        assert len(infos) == 1
        assert isinstance(infos[0], LifeCycleInfo)
        assert infos[0].getLcObjectRef().getValue() == "ActrSts1"
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef().getValue() == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates"

    def test_read_default_periods_only(self, parser):
        """Test that the DEFAULT-PERIOD wrappers are read as LifeCyclePeriod values while the refs stay None."""
        info_set = _new_info_set()
        parser.readLifeCycleInfoSet(_set_element(_PERIODS_ONLY_INNER), info_set)
        assert isinstance(info_set.getDefaultPeriodBegin(), LifeCyclePeriod)
        assert info_set.getDefaultPeriodBegin().getDate().getValue() == "2023-01-01T00:00:00+01:00"
        assert isinstance(info_set.getDefaultPeriodEnd().getProductRelease(), RevisionLabelString)
        assert info_set.getDefaultPeriodEnd().getProductRelease().getValue() == "1.0.0"
        assert info_set.getDefaultLcStateRef() is None
        assert info_set.getLifeCycleInfos() == []
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef() is None

    def test_read_absent_optional_fields(self, parser):
        """Test that a bare LIFE-CYCLE-INFO-SET leaves every field empty (the empty-wrapper case)."""
        info_set = _new_info_set()
        parser.readLifeCycleInfoSet(_set_element(""), info_set)
        assert info_set.getDefaultLcStateRef() is None
        assert info_set.getDefaultPeriodBegin() is None
        assert info_set.getDefaultPeriodEnd() is None
        assert info_set.getLifeCycleInfos() == []
        assert info_set.getUsedLifeCycleStateDefinitionGroupRef() is None

    def test_read_empty_infos_wrapper(self, parser):
        """Test that an empty LIFE-CYCLE-INFOS wrapper yields an empty lifeCycleInfos list."""
        info_set = _new_info_set()
        parser.readLifeCycleInfoSet(_set_element("<LIFE-CYCLE-INFOS></LIFE-CYCLE-INFOS>"), info_set)
        assert info_set.getLifeCycleInfos() == []
