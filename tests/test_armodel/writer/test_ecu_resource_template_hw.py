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
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, RefType
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
