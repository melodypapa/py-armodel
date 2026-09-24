"""Writer round-trip tests for LifeCycleInfoSet (element order per XSD group LIFE-CYCLE-INFO-SET, AUTOSAR_00052.xsd L76621: DEFAULT-LC-STATE-REF, DEFAULT-PERIOD-BEGIN, DEFAULT-PERIOD-END, LIFE-CYCLE-INFOS, USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, RefType, RevisionLabelString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import LifeCycleInfo, LifeCyclePeriod
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


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _period(date: str, **kwargs) -> LifeCyclePeriod:
    period = LifeCyclePeriod()
    period.setDate(DateTime().setValue(date))
    if "ar_release_version" in kwargs:
        period.setArReleaseVersion(RevisionLabelString().setValue(kwargs["ar_release_version"]))
    if "product_release" in kwargs:
        period.setProductRelease(RevisionLabelString().setValue(kwargs["product_release"]))
    return period


def _new_info_set():
    info_set = _pkg().createLifeCycleInfoSet("LcSet")
    info_set.setDefaultLcStateRef(_ref("/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/valid", "LIFE-CYCLE-STATE"))
    info_set.setDefaultPeriodBegin(_period("2023-01-01T00:00:00+01:00", ar_release_version="4.3.1"))
    info_set.setDefaultPeriodEnd(_period("2024-12-31T23:59:59+01:00", product_release="1.0.0"))

    info = LifeCycleInfo()
    info.setLcObjectRef(_ref("ActrSts1", "APPLICATION-RECORD-DATA-TYPE"))
    info_set.addLifeCycleInfo(info)

    info_set.setUsedLifeCycleStateDefinitionGroupRef(_ref("/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates", "LIFE-CYCLE-STATE-DEFINITION-GROUP"))
    return info_set


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    idx = xml_str.find(">")
    xml_str = xml_str[:idx] + f' xmlns="{NS}"' + xml_str[idx:]
    return ET.fromstring(xml_str)


class TestWriteLifeCycleInfoSet:
    def test_write_element_order(self, writer):
        """Test that the written XML children follow the XSD group order after SHORT-NAME."""
        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfoSet(parent, _new_info_set())
        set_element = parent.find("LIFE-CYCLE-INFO-SET")
        assert set_element is not None
        assert [child.tag for child in set_element] == [
            "SHORT-NAME",
            "DEFAULT-LC-STATE-REF",
            "DEFAULT-PERIOD-BEGIN",
            "DEFAULT-PERIOD-END",
            "LIFE-CYCLE-INFOS",
            "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF",
        ]
        assert set_element.find("DEFAULT-LC-STATE-REF").text == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/valid"
        assert set_element.find("DEFAULT-PERIOD-BEGIN/DATE").text == "2023-01-01T00:00:00+01:00"
        assert set_element.find("DEFAULT-PERIOD-BEGIN/AR-RELEASE-VERSION").text == "4.3.1"
        assert set_element.find("DEFAULT-PERIOD-END/DATE").text == "2024-12-31T23:59:59+01:00"
        assert set_element.find("DEFAULT-PERIOD-END/PRODUCT-RELEASE").text == "1.0.0"
        assert [ref.text for ref in set_element.findall("LIFE-CYCLE-INFOS/LIFE-CYCLE-INFO/LC-OBJECT-REF")] == ["ActrSts1"]
        assert set_element.find("USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF").text == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates"

    def test_write_none(self, writer):
        """Test that a None LifeCycleInfoSet writes no element."""
        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfoSet(parent, None)
        assert len(parent) == 0

    def test_write_empty_wrapper(self, writer):
        """Test that a LifeCycleInfoSet with no fields writes only the SHORT-NAME child."""
        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfoSet(parent, _pkg().createLifeCycleInfoSet("EmptySet"))
        set_element = parent.find("LIFE-CYCLE-INFO-SET")
        assert set_element is not None
        assert [child.tag for child in set_element] == ["SHORT-NAME"]

    def test_round_trip_values_preserved(self, writer, parser):
        """Test parse -> write -> re-parse preserves every field value including the DEFAULT-PERIOD wrappers."""
        parsed = _pkg().createLifeCycleInfoSet("RtSet")
        source = ET.fromstring(
            f"<PARENT xmlns='{NS}'>"
            "<LIFE-CYCLE-INFO-SET>"
            "<SHORT-NAME>RtSet</SHORT-NAME>"
            '<DEFAULT-LC-STATE-REF DEST="LIFE-CYCLE-STATE">/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/valid</DEFAULT-LC-STATE-REF>'
            "<DEFAULT-PERIOD-BEGIN><DATE>2023-01-01T00:00:00+01:00</DATE><AR-RELEASE-VERSION>4.3.1</AR-RELEASE-VERSION></DEFAULT-PERIOD-BEGIN>"
            "<DEFAULT-PERIOD-END><DATE>2024-12-31T23:59:59+01:00</DATE><PRODUCT-RELEASE>1.0.0</PRODUCT-RELEASE></DEFAULT-PERIOD-END>"
            '<LIFE-CYCLE-INFOS><LIFE-CYCLE-INFO><LC-OBJECT-REF DEST="APPLICATION-RECORD-DATA-TYPE">ActrSts1</LC-OBJECT-REF></LIFE-CYCLE-INFO></LIFE-CYCLE-INFOS>'
            '<USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF DEST="LIFE-CYCLE-STATE-DEFINITION-GROUP">/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates</USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF>'
            "</LIFE-CYCLE-INFO-SET>"
            "</PARENT>"
        )
        parser.readLifeCycleInfoSet(source[0], parsed)

        parent = ET.Element("PARENT")
        writer.writeLifeCycleInfoSet(parent, parsed)
        set_element = parent.find("LIFE-CYCLE-INFO-SET")
        assert [child.tag for child in set_element] == [
            "SHORT-NAME",
            "DEFAULT-LC-STATE-REF",
            "DEFAULT-PERIOD-BEGIN",
            "DEFAULT-PERIOD-END",
            "LIFE-CYCLE-INFOS",
            "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF",
        ]

        reparsed = _pkg().createLifeCycleInfoSet("RtSet2")
        parser.readLifeCycleInfoSet(_round_trip(parent)[0], reparsed)
        assert reparsed.getDefaultLcStateRef().getValue() == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates/valid"
        assert reparsed.getDefaultPeriodBegin().getDate().getValue() == "2023-01-01T00:00:00+01:00"
        assert reparsed.getDefaultPeriodBegin().getArReleaseVersion().getValue() == "4.3.1"
        assert reparsed.getDefaultPeriodEnd().getDate().getValue() == "2024-12-31T23:59:59+01:00"
        assert reparsed.getDefaultPeriodEnd().getProductRelease().getValue() == "1.0.0"
        assert reparsed.getLifeCycleInfos()[0].getLcObjectRef().getValue() == "ActrSts1"
        assert reparsed.getUsedLifeCycleStateDefinitionGroupRef().getValue() == "/AUTOSAR/GenDef/LifeCycleStateDefinitionGroups/AutosarLifeCycleStates"
