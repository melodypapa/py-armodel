"""Reader tests for LifeCycleInfo (LIFE-CYCLE-INFO per XSD group AUTOSAR_00052.xsd L76529: LC-OBJECT-REF, LC-STATE-REF, PERIOD-BEGIN, PERIOD-END, REMARK, USE-INSTEAD-REFS)."""

import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCycleInfoSet, LifeCyclePeriod
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

_FULL_INFO_INNER = (
    '<LC-OBJECT-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSts1</LC-OBJECT-REF>'
    '<LC-STATE-REF DEST="LIFE-CYCLE-STATE">/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/obsolete</LC-STATE-REF>'
    "<PERIOD-BEGIN>"
    "<DATE>2023-06-15T12:00:00+01:00</DATE>"
    "<AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION>"
    "</PERIOD-BEGIN>"
    "<PERIOD-END>"
    "<DATE>2024-01-01T00:00:00+01:00</DATE>"
    "<PRODUCT-RELEASE>1.2.3</PRODUCT-RELEASE>"
    "</PERIOD-END>"
    "<REMARK><P><L-1>why the element was given the specified life cycle</L-1></P></REMARK>"
    "<USE-INSTEAD-REFS>"
    '<USE-INSTEAD-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSt1</USE-INSTEAD-REF>'
    '<USE-INSTEAD-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSt2</USE-INSTEAD-REF>'
    "</USE-INSTEAD-REFS>"
)

_FULL_INFO = f"<LIFE-CYCLE-INFO>{_FULL_INFO_INNER}</LIFE-CYCLE-INFO>"

_FULL_INFO_SET = f"<LIFE-CYCLE-INFOS><LIFE-CYCLE-INFO>{_FULL_INFO_INNER}</LIFE-CYCLE-INFO></LIFE-CYCLE-INFOS>"


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


def _info_element(inner_xml: str) -> ET.Element:
    return ET.fromstring(f"<LIFE-CYCLE-INFO xmlns='{NS}'>{inner_xml}</LIFE-CYCLE-INFO>")


class TestReadLifeCycleInfo:
    def test_read_all_fields(self, parser):
        """Test that all six LIFE-CYCLE-INFO children are read with their spec types and values."""
        info = LifeCycleInfo()
        parser.readLifeCycleInfo(_info_element(_FULL_INFO_INNER), info)
        assert info.getLcObjectRef().getValue() == "ActrSts1"
        assert info.getLcStateRef().getValue() == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/obsolete"
        assert isinstance(info.getPeriodBegin(), LifeCyclePeriod)
        assert info.getPeriodBegin().getDate().getValue() == "2023-06-15T12:00:00+01:00"
        assert info.getPeriodBegin().getArReleaseVersion().getValue() == "4.3.1"
        assert isinstance(info.getPeriodEnd(), LifeCyclePeriod)
        assert info.getPeriodEnd().getDate().getValue() == "2024-01-01T00:00:00+01:00"
        assert info.getPeriodEnd().getProductRelease().getValue() == "1.2.3"
        assert isinstance(info.getRemark(), DocumentationBlock)
        assert [ref.getValue() for ref in info.getUseInsteadRefs()] == ["ActrSt1", "ActrSt2"]

    def test_read_period_end(self, parser):
        """Test that PERIOD-END is read as a LifeCyclePeriod with its DATE and PRODUCT-RELEASE."""
        info = LifeCycleInfo()
        parser.readLifeCycleInfo(
            _info_element("<PERIOD-END>" "<DATE>2024-01-01T00:00:00+01:00</DATE>" "<PRODUCT-RELEASE>1.2.3</PRODUCT-RELEASE>" "</PERIOD-END>"),
            info,
        )
        assert isinstance(info.getPeriodEnd(), LifeCyclePeriod)
        assert info.getPeriodEnd().getDate().getValue() == "2024-01-01T00:00:00+01:00"
        assert isinstance(info.getPeriodEnd().getProductRelease(), RevisionLabelString)
        assert info.getPeriodEnd().getProductRelease().getValue() == "1.2.3"

    def test_read_absent_optional_fields(self, parser):
        """Test that a bare LIFE-CYCLE-INFO leaves every field empty (the empty-wrapper case)."""
        info = LifeCycleInfo()
        parser.readLifeCycleInfo(_info_element(""), info)
        assert info.getLcObjectRef() is None
        assert info.getLcStateRef() is None
        assert info.getPeriodBegin() is None
        assert info.getPeriodEnd() is None
        assert info.getRemark() is None
        assert info.getUseInsteadRefs() == []

    def test_read_through_life_cycle_info_set(self, parser):
        """Test that readLifeCycleInfoSetLifeCycleInfos dispatches readLifeCycleInfo and populates field values."""
        info_set = LifeCycleInfoSet(parent=MagicMock(), short_name="lcis")
        parser.readLifeCycleInfoSetLifeCycleInfos(_parent_with(_FULL_INFO_SET), info_set)
        infos = info_set.getLifeCycleInfos()
        assert len(infos) == 1
        assert infos[0].getLcObjectRef().getValue() == "ActrSts1"
        assert isinstance(infos[0].getPeriodEnd(), LifeCyclePeriod)
        assert infos[0].getPeriodEnd().getDate().getValue() == "2024-01-01T00:00:00+01:00"
        assert [ref.getValue() for ref in infos[0].getUseInsteadRefs()] == ["ActrSt1", "ActrSt2"]
