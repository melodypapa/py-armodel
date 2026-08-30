"""
Tests for writing ARPackage REFERENCE-BASES elements — Table 4.1 (referenceBase aggregation).

Round-trip counterpart: tests/test_armodel/parser/test_ar_package_reference_bases.py
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ReferenceBase,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    RefType,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteReferenceBases:
    """
    Test writeReferenceBases (ARPackage.referenceBase, Table 4.1).
    """

    def test_write_reference_base_fields(self):
        """
        Test that every ReferenceBase field value is written to its own element
        (IS-GLOBAL must come from getIsGlobal, IS-DEFAULT from getIsDefault).
        """
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        base = ReferenceBase()
        base.setShortLabel(Identifier().setValue("DefaultBase"))
        base.setIsDefault(Boolean().setValue(True))
        base.setIsGlobal(Boolean().setValue(False))
        base.setBaseIsThisPackage(Boolean().setValue(True))
        base.setPackageRef(RefType().setValue("/AUTOSAR/TestPackage"))

        writer.writeReferenceBases(element, [base])

        bases_tag = element.find("REFERENCE-BASES")
        assert bases_tag is not None
        base_tag = bases_tag.find("REFERENCE-BASE")
        assert base_tag is not None
        assert base_tag.find("SHORT-LABEL").text == "DefaultBase"
        assert base_tag.find("IS-DEFAULT").text == "true"
        assert base_tag.find("IS-GLOBAL").text == "false"
        assert base_tag.find("BASE-IS-THIS-PACKAGE").text == "true"
        assert base_tag.find("PACKAGE-REF").text == "/AUTOSAR/TestPackage"

    def test_write_empty_reference_bases(self):
        """
        Test that an empty reference base list writes no REFERENCE-BASES wrapper.
        """
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        writer.writeReferenceBases(element, [])

        assert element.find("REFERENCE-BASES") is None
