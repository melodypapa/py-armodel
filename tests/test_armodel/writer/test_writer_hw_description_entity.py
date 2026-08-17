"""Tests for reading and writing HwDescriptionEntity attributes."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeValue
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementConnector import HwElementConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _build_document(element: HwElement):
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    ar_root = document.createARPackage("AUTOSAR")
    ar_root.addElement(element)
    return document


def _reload(file_path):
    document_2 = AUTOSAR.getInstance()
    document_2.clear()
    ARXMLParser().load(file_path, document_2)
    package = document_2.getARPackages()[0]
    return next(element for element in package.elements if isinstance(element, HwElement))


class TestWriteHwDescriptionEntity:
    def test_round_trip_populated(self):
        """Test parse -> write -> re-parse of populated hwTypeRef, hwCategoryRefs, hwAttributeValues."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = HwElement(ar_root, "TestElement")

        element.setHwTypeRef(make_ref("/HwTypes/TestType", "HW-TYPE"))
        element.addHwCategoryRef(make_ref("/HwCategories/Cat1", "HW-CATEGORY"))
        element.addHwCategoryRef(make_ref("/HwCategories/Cat2", "HW-CATEGORY"))

        attribute_value = HwAttributeValue()
        attribute_value.setHwAttributeDefRef(make_ref("/HwCategories/Cat1/AttrDef", "HW-ATTRIBUTE-DEF"))
        element.addHwAttributeValue(attribute_value)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(element))
            element_2 = _reload(file_path)
            assert element_2.getShortName() == "TestElement"
            assert element_2.getHwTypeRef().getValue() == "/HwTypes/TestType"
            assert element_2.getHwTypeRef().getDest() == "HW-TYPE"
            category_refs = element_2.getHwCategoryRefs()
            assert len(category_refs) == 2
            assert [r.getValue() for r in category_refs] == ["/HwCategories/Cat1", "/HwCategories/Cat2"]
            attribute_values = element_2.getHwAttributeValues()
            assert len(attribute_values) == 1
            assert attribute_values[0].getHwAttributeDefRef().getValue() == "/HwCategories/Cat1/AttrDef"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_emits_no_wrappers(self):
        """Test empty refs/lists round-trip to no wrapper elements."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = HwElement(ar_root, "TestElement")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(element))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "HW-TYPE-REF" not in content
            assert "HW-CATEGORY-REFS" not in content
            assert "HW-ATTRIBUTE-VALUES" not in content
            assert "HW-ELEMENT-CONNECTIONS" not in content
            assert "NESTED-ELEMENTS" not in content

            element_2 = _reload(file_path)
            assert element_2.getShortName() == "TestElement"
            assert element_2.getHwTypeRef() is None
            assert element_2.getHwCategoryRefs() == []
            assert element_2.getHwAttributeValues() == []
            assert element_2.getHwElementConnections() == []
            assert element_2.getNestedElementRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_connections_and_nested(self):
        """Test parse -> write -> re-parse of hwElementConnection and nestedElement."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        element = HwElement(ar_root, "TestElement")

        connector = HwElementConnector()
        connector.setHwElementRef(make_ref("/Elements/ElemA", "HW-ELEMENT"))
        connector.setHwPinRef(make_ref("/Elements/ElemA/Pin1", "HW-PIN"))
        element.addHwElementConnection(connector)
        element.addNestedElementRef(make_ref("/Elements/ElemB", "HW-ELEMENT"))
        element.addNestedElementRef(make_ref("/Elements/ElemC", "HW-ELEMENT"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(element))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "HW-ELEMENT-CONNECTIONS" in content
            assert "HW-ELEMENT-CONNECTOR" in content
            assert "NESTED-ELEMENTS" in content

            element_2 = _reload(file_path)
            connections = element_2.getHwElementConnections()
            assert len(connections) == 1
            assert connections[0].getHwElementRef().getValue() == "/Elements/ElemA"
            assert connections[0].getHwElementRef().getDest() == "HW-ELEMENT"
            assert connections[0].getHwPinRef().getValue() == "/Elements/ElemA/Pin1"
            assert connections[0].getHwPinRef().getDest() == "HW-PIN"
            nested = element_2.getNestedElementRefs()
            assert len(nested) == 2
            assert [ref.getValue() for ref in nested] == ["/Elements/ElemB", "/Elements/ElemC"]
            assert all(ref.getDest() == "HW-ELEMENT" for ref in nested)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
