"""Writer round-trip tests for LifeCycleInfo (element order per XSD group LIFE-CYCLE-INFO, AUTOSAR_00052.xsd L76529: LC-OBJECT-REF, LC-STATE-REF, PERIOD-BEGIN, PERIOD-END, REMARK, USE-INSTEAD-REFS)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCyclePeriod
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LEnum, LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _ref(value: str, dest: str = "APPLICATION-RECORD-DATA-TYPE") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _remark() -> DocumentationBlock:
    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL(LEnum.EN)
    l1.setValue("why the element was given the specified life cycle")
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block


def _new_info() -> LifeCycleInfo:
    info = LifeCycleInfo()
    info.setLcObjectRef(_ref("ActrSts1"))
    info.setLcStateRef(_ref("/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/obsolete", "LIFE-CYCLE-STATE"))

    begin = LifeCyclePeriod()
    begin.setDate(DateTime().setValue("2023-06-15T12:00:00+01:00"))
    begin.setArReleaseVersion(RevisionLabelString().setValue("4.3.1"))
    info.setPeriodBegin(begin)

    end = LifeCyclePeriod()
    end.setDate(DateTime().setValue("2024-01-01T00:00:00+01:00"))
    end.setProductRelease(RevisionLabelString().setValue("1.2.3"))
    info.setPeriodEnd(end)

    info.setRemark(_remark())
    info.addUseInsteadRef(_ref("ActrSt1"))
    info.addUseInsteadRef(_ref("ActrSt2"))
    return info


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    if xml_str.rstrip().endswith("/>"):
        xml_str = xml_str.rstrip()[:-2].rstrip() + f' xmlns="{NS}"/>'
    else:
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + f' xmlns="{NS}"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestWriteLifeCycleInfo:
    def test_write_element_order(self, writer):
        """Test that the written XML children follow the XSD group order LC-OBJECT-REF, LC-STATE-REF, PERIOD-BEGIN, PERIOD-END, REMARK, USE-INSTEAD-REFS."""
        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfo(parent, _new_info())
        info_element = parent.find("LIFE-CYCLE-INFO")
        assert info_element is not None
        assert [child.tag for child in info_element] == [
            "LC-OBJECT-REF",
            "LC-STATE-REF",
            "PERIOD-BEGIN",
            "PERIOD-END",
            "REMARK",
            "USE-INSTEAD-REFS",
        ]
        assert info_element.find("LC-OBJECT-REF").text == "ActrSts1"
        assert info_element.find("LC-OBJECT-REF").attrib["DEST"] == "APPLICATION-RECORD-DATA-TYPE"
        assert info_element.find("PERIOD-BEGIN/DATE").text == "2023-06-15T12:00:00+01:00"
        assert info_element.find("PERIOD-END/DATE").text == "2024-01-01T00:00:00+01:00"
        assert info_element.find("PERIOD-END/PRODUCT-RELEASE").text == "1.2.3"
        assert info_element.find("REMARK/P/L-1").text == "why the element was given the specified life cycle"
        assert [ref.text for ref in info_element.findall("USE-INSTEAD-REFS/USE-INSTEAD-REF")] == ["ActrSt1", "ActrSt2"]

    def test_write_none(self, writer):
        """Test that a None LifeCycleInfo writes no element."""
        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfo(parent, None)
        assert len(parent) == 0

    def test_write_empty_wrapper(self, writer):
        """Test that a LifeCycleInfo with no fields writes a bare empty element."""
        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfo(parent, LifeCycleInfo())
        info_element = parent.find("LIFE-CYCLE-INFO")
        assert info_element is not None
        assert len(list(info_element)) == 0

    def test_round_trip_values_preserved(self, writer, parser):
        """Test parse -> write -> re-parse preserves every field value including PERIOD-END."""
        parent_element = ET.fromstring(
            f"<PARENT xmlns='{NS}'>"
            "<LIFE-CYCLE-INFO>"
            '<LC-OBJECT-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSts1</LC-OBJECT-REF>'
            "<PERIOD-BEGIN><DATE>2023-06-15T12:00:00+01:00</DATE><AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION></PERIOD-BEGIN>"
            "<PERIOD-END><DATE>2024-01-01T00:00:00+01:00</DATE><PRODUCT-RELEASE>1.2.3</PRODUCT-RELEASE></PERIOD-END>"
            "<REMARK><P><L-1>why the element was given the specified life cycle</L-1></P></REMARK>"
            '<USE-INSTEAD-REFS><USE-INSTEAD-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSt1</USE-INSTEAD-REF></USE-INSTEAD-REFS>'
            "</LIFE-CYCLE-INFO>"
            "</PARENT>"
        )
        parsed = LifeCycleInfo()
        parser.readLifeCycleInfo(parent_element[0], parsed)

        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfo(parent, parsed)
        info_element = parent.find("LIFE-CYCLE-INFO")
        assert [child.tag for child in info_element] == [
            "LC-OBJECT-REF",
            "PERIOD-BEGIN",
            "PERIOD-END",
            "REMARK",
            "USE-INSTEAD-REFS",
        ]
        assert info_element.find("LC-OBJECT-REF").text == "ActrSts1"
        assert info_element.find("PERIOD-END/DATE").text == "2024-01-01T00:00:00+01:00"

        reparsed = LifeCycleInfo()
        parser.readLifeCycleInfo(_round_trip(parent)[0], reparsed)
        assert reparsed.getLcObjectRef().getValue() == "ActrSts1"
        assert reparsed.getPeriodBegin().getDate().getValue() == "2023-06-15T12:00:00+01:00"
        assert reparsed.getPeriodBegin().getArReleaseVersion().getValue() == "4.3.1"
        assert isinstance(reparsed.getPeriodEnd(), LifeCyclePeriod)
        assert reparsed.getPeriodEnd().getDate().getValue() == "2024-01-01T00:00:00+01:00"
        assert reparsed.getPeriodEnd().getProductRelease().getValue() == "1.2.3"
        assert reparsed.getRemark() is not None
        assert [ref.getValue() for ref in reparsed.getUseInsteadRefs()] == ["ActrSt1"]
