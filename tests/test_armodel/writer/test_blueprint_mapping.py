"""
Tests for writing BLUEPRINT-MAPPING elements (BlueprintMapping, R23-11 Table C.17).

XSD 00052 group BLUEPRINT-MAPPING element order: BLUEPRINT-REF -> DERIVED-OBJECT-REF.
Round-trip counterpart: tests/test_armodel/parser/test_blueprint_mapping.py
Set-level dispatch: tests/test_armodel/writer/test_blueprint_mapping_set.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteBlueprintMapping:
    """
    Test writeBlueprintMapping (BlueprintMapping.blueprint/derivedObject, Table C.17).
    """

    def test_write_blueprint_mapping_refs(self):
        """Test that both refs are written in XSD order BLUEPRINT-REF -> DERIVED-OBJECT-REF with values and DEST."""
        writer = _make_writer()
        element = ET.Element("BLUEPRINT-MAPS")

        mapping = BlueprintMapping()
        blueprint_ref = RefType()
        blueprint_ref.setDest("ECUC-MODULE-DEF")
        blueprint_ref.setValue("/Pkg/Blueprint")
        mapping.setBlueprintRef(blueprint_ref)
        derived_ref = RefType()
        derived_ref.setDest("COMPU-METHOD")
        derived_ref.setValue("/Pkg/Derived")
        mapping.setDerivedObjectRef(derived_ref)

        mapping_tag = ET.SubElement(element, "BLUEPRINT-MAPPING")
        writer.writeBlueprintMapping(mapping_tag, mapping)

        assert [child.tag for child in mapping_tag] == ["BLUEPRINT-REF", "DERIVED-OBJECT-REF"]
        blueprint_tag = mapping_tag.find("BLUEPRINT-REF")
        assert blueprint_tag.attrib["DEST"] == "ECUC-MODULE-DEF"
        assert blueprint_tag.text == "/Pkg/Blueprint"
        derived_tag = mapping_tag.find("DERIVED-OBJECT-REF")
        assert derived_tag.attrib["DEST"] == "COMPU-METHOD"
        assert derived_tag.text == "/Pkg/Derived"

    def test_write_blueprint_mapping_none_writes_no_elements(self):
        """Test that a BlueprintMapping without refs writes no ref elements."""
        writer = _make_writer()
        element = ET.Element("BLUEPRINT-MAPS")

        mapping_tag = ET.SubElement(element, "BLUEPRINT-MAPPING")
        writer.writeBlueprintMapping(mapping_tag, BlueprintMapping())

        assert list(mapping_tag) == []

    def test_round_trip_with_refs(self):
        """Build a model, write it, reparse, and assert both ref values survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        bms = ar_root.createBlueprintMappingSet("MySet")

        mapping = BlueprintMapping()
        blueprint_ref = RefType()
        blueprint_ref.setDest("ECUC-MODULE-DEF")
        blueprint_ref.setValue("/Pkg/Blueprint")
        mapping.setBlueprintRef(blueprint_ref)
        derived_ref = RefType()
        derived_ref.setDest("COMPU-METHOD")
        derived_ref.setValue("/Pkg/Derived")
        mapping.setDerivedObjectRef(derived_ref)
        bms.addBlueprintMap(mapping)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            from armodel.parser.arxml_parser import ARXMLParser

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            bms_2 = document_2.getARPackages()[0].getBlueprintMappingSets()[0]
            maps = bms_2.getBlueprintMaps()
            assert len(maps) == 1
            assert isinstance(maps[0], BlueprintMapping)
            assert maps[0].getBlueprintRef().getValue() == "/Pkg/Blueprint"
            assert maps[0].getDerivedObjectRef().getDest() == "COMPU-METHOD"
        finally:
            os.remove(file_path)
