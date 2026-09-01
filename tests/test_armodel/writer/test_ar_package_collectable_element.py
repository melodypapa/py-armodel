"""
Writer coverage for the CollectableElement inheritance path (Table 13.3).

CollectableElement contributes no XML of its own: Table 13.3 has no Attribute rows
and the AUTOSAR_00052.xsd group COLLECTABLE-ELEMENT is an empty `<xsd:sequence/>`.
Its writer coverage is therefore the shared writeIdentifiable chain plus the
element-collection registry, both reached through its concrete subclass ARPackage
(and PackageableElement/ARElement below it).

Round-trip counterpart: tests/test_armodel/parser/test_ar_package_collectable_element.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString, String
from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "DCE:6f1c0e0e-1111-2222-3333-444455556666"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_writer():
    from armodel.writer.arxml_writer import ARXMLWriter

    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


def _build_document() -> ARPackage:
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    ar_root = document.createARPackage("AUTOSAR")
    package = ar_root.createARPackage("TestPackage")
    package.setUuid(String().setValue(UUID_VALUE))
    package.setCategory(CategoryString().setValue("STANDARD"))
    package.createARPackage("SubPackage")
    package.createSwBaseType("MyBaseType")
    return package


class TestWriteCollectableElementPath:
    """
    Test that the Identifiable members and the element-collection registry inherited
    by a concrete CollectableElement subclass (ARPackage) are written back out.
    """

    def test_write_ar_package_shape(self):
        """
        The written AR-PACKAGE carries the Identifiable attributes, the sub packages
        and the contained elements.
        """
        package = _build_document()
        element = ET.Element("AR-PACKAGES")

        _make_writer().writeARPackage(element, package)

        package_tag = element.find("AR-PACKAGE")
        assert package_tag is not None
        assert package_tag.find("SHORT-NAME").text == "TestPackage"
        assert package_tag.get("UUID") == UUID_VALUE
        assert package_tag.find("CATEGORY").text == "STANDARD"
        assert package_tag.find("AR-PACKAGES/AR-PACKAGE/SHORT-NAME").text == "SubPackage"
        assert package_tag.find("ELEMENTS/SW-BASE-TYPE/SHORT-NAME").text == "MyBaseType"

    def test_round_trip(self):
        """
        Write an ARPackage, reparse it, and assert the inherited members and the
        element registry survive the round trip.
        """
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        _build_document()

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, AUTOSAR.getInstance())

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            ar_root_2 = document_2.getARPackages()[0]
            package_2 = ar_root_2.getElement("TestPackage", ARPackage)
            assert package_2 is not None
            assert package_2.getShortName() == "TestPackage"
            assert package_2.getUuid() is not None
            assert package_2.getUuid().getValue() == UUID_VALUE
            assert package_2.getCategory() is not None
            assert package_2.getCategory().getValue() == "STANDARD"

            sub_package_2 = package_2.getElement("SubPackage", ARPackage)
            assert sub_package_2 is not None
            assert sub_package_2.getShortName() == "SubPackage"

            base_type_2 = package_2.getElement("MyBaseType", SwBaseType)
            assert base_type_2 is not None
            assert base_type_2.getShortName() == "MyBaseType"
            assert package_2.getTotalElement() == 1
            assert package_2.getElements() == [base_type_2]
        finally:
            os.remove(file_path)
