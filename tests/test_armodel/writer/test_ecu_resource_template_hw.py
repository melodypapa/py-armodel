"""Reader/writer round-trip tests for the EcuResourceTemplate Hw* family.

XML element order per the XSD groups (AUTOSAR_00052.xsd):
- HW-DESCRIPTION-ENTITY (l.65772): HW-TYPE-REF, HW-CATEGORY-REFS, HW-ATTRIBUTE-VALUES.
- HW-ELEMENT-CONNECTOR (l.65909): HW-ELEMENT-REFS, HW-PIN-GROUP-CONNECTIONS, HW-PIN-CONNECTIONS
  (the trailing VARIATION-POINT element is an atpVariation artifact and is not modeled).
- HW-PIN-GROUP-CONNECTOR (l.66193): HW-PIN-CONNECTIONS, HW-PIN-GROUP-REFS.
- HW-PIN-CONNECTOR (l.66093): HW-PIN-REFS.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement, HwElementConnector, HwPinConnector, HwPinGroup, HwPinGroupConnector, HwPinGroupContent
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, Numerical, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _save_and_reload(element: HwElement) -> HwElement:
    document = AUTOSAR.getInstance()
    ar_root = document.createARPackage("AUTOSAR")
    ar_root.addReferrableElement(element)
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)
        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        package = document_2.getARPackages()[0]
        return next(e for e in package.referrableElements if isinstance(e, HwElement))
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def _strip_ns(tag: str) -> str:
    return tag.split("}")[-1]


class TestHwDescriptionEntityReadWrite:
    def test_round_trip_attribute_values_with_nested_value(self):
        """hwTypeRef, hwCategoryRefs and hwAttributeValues survive a write/read cycle with field values asserted (Table 2.1)."""
        element = HwElement(None, "TestEntity")
        element.setHwTypeRef(make_ref("/HwTypes/TestType", "HW-TYPE"))
        element.addHwCategoryRef(make_ref("/HwCategories/Cat1", "HW-CATEGORY"))
        attribute_value = HwAttributeValue()
        attribute_value.setHwAttributeDefRef(make_ref("/HwCategories/Cat1/AttrDef", "HW-ATTRIBUTE-DEF"))
        numerical = Numerical()
        numerical.setValue("42")
        attribute_value.setV(numerical)
        element.addHwAttributeValue(attribute_value)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwElement(parent, element)
        hw_element = parent.find("HW-ELEMENT")
        assert [_strip_ns(e.tag) for e in hw_element] == ["SHORT-NAME", "HW-TYPE-REF", "HW-CATEGORY-REFS", "HW-ATTRIBUTE-VALUES"]
        attribute_values_element = hw_element.find("HW-ATTRIBUTE-VALUES")
        assert [_strip_ns(e.tag) for e in attribute_values_element] == ["HW-ATTRIBUTE-VALUE"]
        assert [_strip_ns(e.tag) for e in attribute_values_element.find("HW-ATTRIBUTE-VALUE")] == ["HW-ATTRIBUTE-DEF-REF", "V"]

        element_2 = _save_and_reload(element)
        assert element_2.getHwTypeRef().getValue() == "/HwTypes/TestType"
        assert element_2.getHwTypeRef().getDest() == "HW-TYPE"
        assert [r.getValue() for r in element_2.getHwCategoryRefs()] == ["/HwCategories/Cat1"]
        attribute_values = element_2.getHwAttributeValues()
        assert len(attribute_values) == 1
        assert attribute_values[0].getHwAttributeDefRef().getValue() == "/HwCategories/Cat1/AttrDef"
        assert attribute_values[0].getV().getValue() == 42

    def test_round_trip_unset_emits_no_wrappers(self):
        """An entity with no attribute values emits no HW-TYPE-REF/HW-CATEGORY-REFS/HW-ATTRIBUTE-VALUES elements and reloads empty."""
        element = HwElement(None, "TestEntity")

        element_2 = _save_and_reload(element)
        assert element_2.getHwTypeRef() is None
        assert element_2.getHwCategoryRefs() == []
        assert element_2.getHwAttributeValues() == []


class TestHwPinGroupContentReadWrite:
    def _make_pin(self, hw_pin_group: HwPinGroup, short_name: str, function_name: str) -> None:
        pin_group_content = HwPinGroupContent()
        hw_pin_group.setHwPinGroupContent(pin_group_content)
        pin = pin_group_content.createHwPin(short_name)
        pin.addFunctionName(function_name)
        pin.setPackagingPinName("A03")
        pin_number = Integer()
        pin_number.setValue("3")
        pin.setPinNumber(pin_number)

    def test_round_trip_nested_pin_group_content(self):
        """HW-PIN-GROUP-CONTENT with a nested HwPin survives a write/read cycle with field values asserted (Table 2.6 via HwPinGroup Table 2.5)."""
        element = HwElement(None, "TestEntity")
        pin_group = element.createHwPinGroup("Group1")
        self._make_pin(pin_group, "Pin1", "CLK")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwElement(parent, element)
        hw_element = parent.find("HW-ELEMENT")
        pin_groups_element = hw_element.find("HW-PIN-GROUPS")
        pin_group_element = pin_groups_element.find("HW-PIN-GROUP")
        content_element = pin_group_element.find("HW-PIN-GROUP-CONTENT")
        assert content_element is not None
        pin_element = content_element.find("HW-PIN")
        assert pin_element is not None
        assert [_strip_ns(e.tag) for e in pin_element] == ["SHORT-NAME", "FUNCTION-NAMES", "PACKAGING-PIN-NAME", "PIN-NUMBER"]

        element_2 = _save_and_reload(element)
        pin_group_2 = element_2.getHwPinGroups()[0]
        content_2 = pin_group_2.getHwPinGroupContent()
        assert content_2 is not None
        pin_2 = content_2.getHwPin()
        assert pin_2 is not None
        assert pin_2.getShortName() == "Pin1"
        assert [fn for fn in pin_2.getFunctionNames()] == ["CLK"]
        assert pin_2.getPackagingPinName() == "A03"
        assert pin_2.getPinNumber().getValue() == 3

    def test_round_trip_nested_pin_group_in_content(self):
        """A HwPinGroup nested inside HwPinGroupContent survives a write/read cycle (Table 2.6 hwPinGroup 0..1)."""
        element = HwElement(None, "TestEntity")
        outer_group = element.createHwPinGroup("OuterGroup")
        outer_group.setHwPinGroupContent(HwPinGroupContent())
        inner_group = outer_group.getHwPinGroupContent().createHwPinGroup("InnerGroup")
        self._make_pin(inner_group, "Pin1", "CLK")

        element_2 = _save_and_reload(element)
        outer_2 = element_2.getHwPinGroups()[0]
        inner_2 = outer_2.getHwPinGroupContent().getHwPinGroup()
        assert inner_2 is not None
        assert inner_2.getShortName() == "InnerGroup"
        pin_2 = inner_2.getHwPinGroupContent().getHwPin()
        assert pin_2 is not None
        assert pin_2.getShortName() == "Pin1"
        assert pin_2.getFunctionNames() == ["CLK"]

    def test_round_trip_empty_content(self):
        """A HwPinGroup without content emits no HW-PIN-GROUP-CONTENT element; an empty content reloads with both slots None."""
        element = HwElement(None, "TestEntity")
        element.createHwPinGroup("EmptyGroup")

        element_2 = _save_and_reload(element)
        group_2 = element_2.getHwPinGroups()[0]
        assert group_2.getShortName() == "EmptyGroup"
        assert group_2.getHwPinGroupContent() is None


class TestHwElementConnectorReadWrite:
    def test_round_trip_connector_content_and_xsd_order(self):
        """hwElementRefs, hwPinConnections and hwPinGroupConnections survive a write/read cycle; element order per the XSD group HW-ELEMENT-CONNECTOR: HW-ELEMENT-REFS, HW-PIN-GROUP-CONNECTIONS, HW-PIN-CONNECTIONS (Table 2.8)."""
        connector = HwElementConnector()
        connector.addHwElementRef(make_ref("/Elements/ElemA", "HW-ELEMENT"))
        connector.addHwElementRef(make_ref("/Elements/ElemB", "HW-ELEMENT"))
        pin_connector = HwPinConnector()
        pin_connector.addHwPinRef(make_ref("/Elements/ElemA/Pin1", "HW-PIN"))
        connector.addHwPinConnection(pin_connector)
        group_connector = HwPinGroupConnector()
        group_connector.addHwPinGroupRef(make_ref("/Elements/ElemA/Group1", "HW-PIN-GROUP"))
        connector.addHwPinGroupConnection(group_connector)
        element = HwElement(None, "TestEntity")
        element.addHwElementConnection(connector)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwElement(parent, element)
        connector_element = parent.find("HW-ELEMENT").find("HW-ELEMENT-CONNECTIONS").find("HW-ELEMENT-CONNECTOR")
        assert [_strip_ns(e.tag) for e in connector_element] == ["HW-ELEMENT-REFS", "HW-PIN-GROUP-CONNECTIONS", "HW-PIN-CONNECTIONS"]
        assert [_strip_ns(e.tag) for e in connector_element.find("HW-ELEMENT-REFS")] == ["HW-ELEMENT-REF", "HW-ELEMENT-REF"]

        element_2 = _save_and_reload(element)
        connector_2 = element_2.getHwElementConnections()[0]
        assert [r.getValue() for r in connector_2.getHwElementRefs()] == ["/Elements/ElemA", "/Elements/ElemB"]
        assert all(r.getDest() == "HW-ELEMENT" for r in connector_2.getHwElementRefs())
        assert connector_2.getHwPinConnections()[0].getHwPinRefs()[0].getValue() == "/Elements/ElemA/Pin1"
        assert connector_2.getHwPinGroupConnections()[0].getHwPinGroupRefs()[0].getValue() == "/Elements/ElemA/Group1"

    def test_round_trip_empty_connector_wrappers(self):
        """A connector with no content emits no HW-ELEMENT-REFS/HW-PIN-CONNECTIONS/HW-PIN-GROUP-CONNECTIONS wrappers and reloads empty."""
        connector = HwElementConnector()
        element = HwElement(None, "TestEntity")
        element.addHwElementConnection(connector)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwElement(parent, element)
        connector_element = parent.find("HW-ELEMENT").find("HW-ELEMENT-CONNECTIONS").find("HW-ELEMENT-CONNECTOR")
        assert [_strip_ns(e.tag) for e in connector_element] == []

        element_2 = _save_and_reload(element)
        connector_2 = element_2.getHwElementConnections()[0]
        assert connector_2.getHwElementRefs() == []
        assert connector_2.getHwPinConnections() == []
        assert connector_2.getHwPinGroupConnections() == []


class TestHwPinGroupConnectorReadWrite:
    def test_round_trip_group_connector_content_and_xsd_order(self):
        """hwPinConnections and hwPinGroupRefs survive a write/read cycle; element order per the XSD group HW-PIN-GROUP-CONNECTOR: HW-PIN-CONNECTIONS, HW-PIN-GROUP-REFS (Table 2.9)."""
        group_connector = HwPinGroupConnector()
        pin_connector = HwPinConnector()
        pin_connector.addHwPinRef(make_ref("/Elements/ElemA/Pin1", "HW-PIN"))
        group_connector.addHwPinConnection(pin_connector)
        group_connector.addHwPinGroupRef(make_ref("/Elements/ElemA/Group1", "HW-PIN-GROUP"))
        group_connector.addHwPinGroupRef(make_ref("/Elements/ElemA/Group2", "HW-PIN-GROUP"))
        connector = HwElementConnector()
        connector.addHwPinGroupConnection(group_connector)
        element = HwElement(None, "TestEntity")
        element.addHwElementConnection(connector)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwElement(parent, element)
        group_element = parent.find("HW-ELEMENT").find("HW-ELEMENT-CONNECTIONS").find("HW-ELEMENT-CONNECTOR").find("HW-PIN-GROUP-CONNECTIONS").find("HW-PIN-GROUP-CONNECTOR")
        assert [_strip_ns(e.tag) for e in group_element] == ["HW-PIN-CONNECTIONS", "HW-PIN-GROUP-REFS"]
        assert [_strip_ns(e.tag) for e in group_element.find("HW-PIN-GROUP-REFS")] == ["HW-PIN-GROUP-REF", "HW-PIN-GROUP-REF"]

        element_2 = _save_and_reload(element)
        group_2 = element_2.getHwElementConnections()[0].getHwPinGroupConnections()[0]
        assert group_2.getHwPinConnections()[0].getHwPinRefs()[0].getValue() == "/Elements/ElemA/Pin1"
        assert [r.getValue() for r in group_2.getHwPinGroupRefs()] == ["/Elements/ElemA/Group1", "/Elements/ElemA/Group2"]
        assert all(r.getDest() == "HW-PIN-GROUP" for r in group_2.getHwPinGroupRefs())

    def test_round_trip_empty_group_connector_wrappers(self):
        """A group connector with no content emits no HW-PIN-CONNECTIONS/HW-PIN-GROUP-REFS wrappers and reloads empty."""
        connector = HwElementConnector()
        connector.addHwPinGroupConnection(HwPinGroupConnector())
        element = HwElement(None, "TestEntity")
        element.addHwElementConnection(connector)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeHwElement(parent, element)
        group_element = parent.find("HW-ELEMENT").find("HW-ELEMENT-CONNECTIONS").find("HW-ELEMENT-CONNECTOR").find("HW-PIN-GROUP-CONNECTIONS").find("HW-PIN-GROUP-CONNECTOR")
        assert [_strip_ns(e.tag) for e in group_element] == []

        element_2 = _save_and_reload(element)
        group_2 = element_2.getHwElementConnections()[0].getHwPinGroupConnections()[0]
        assert group_2.getHwPinConnections() == []
        assert group_2.getHwPinGroupRefs() == []
