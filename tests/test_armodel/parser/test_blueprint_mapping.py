"""
Tests for parsing BLUEPRINT-MAPPING elements (BlueprintMapping, R23-11 Table C.17).

XSD 00052 group BLUEPRINT-MAPPING element order: BLUEPRINT-REF -> DERIVED-OBJECT-REF.
Round-trip counterpart: tests/test_armodel/writer/test_blueprint_mapping.py
Set-level dispatch: tests/test_armodel/parser/test_blueprint_mapping_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMapping,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


class TestReadBlueprintMapping:
    """
    Test readBlueprintMapping (BlueprintMapping.blueprint/derivedObject, Table C.17).
    """

    def test_read_blueprint_mapping_refs(self, parser):
        """Test that BLUEPRINT-REF and DERIVED-OBJECT-REF populate both fields with values and DEST."""
        mapping = BlueprintMapping()
        element = ET.fromstring(
            f"""<BLUEPRINT-MAPPING xmlns='{NS}'>
                <BLUEPRINT-REF DEST="ECUC-MODULE-DEF">/Pkg/Blueprint</BLUEPRINT-REF>
                <DERIVED-OBJECT-REF DEST="COMPU-METHOD">/Pkg/Derived</DERIVED-OBJECT-REF>
            </BLUEPRINT-MAPPING>"""
        )

        parser.readBlueprintMapping(element, mapping)

        blueprint_ref = mapping.getBlueprintRef()
        assert blueprint_ref is not None
        assert blueprint_ref.getDest() == "ECUC-MODULE-DEF"
        assert blueprint_ref.getValue() == "/Pkg/Blueprint"
        derived_ref = mapping.getDerivedObjectRef()
        assert derived_ref is not None
        assert derived_ref.getDest() == "COMPU-METHOD"
        assert derived_ref.getValue() == "/Pkg/Derived"

    def test_read_blueprint_mapping_empty(self, parser):
        """Test that a bare BLUEPRINT-MAPPING leaves both fields None."""
        mapping = BlueprintMapping()
        element = ET.fromstring(f"<BLUEPRINT-MAPPING xmlns='{NS}'></BLUEPRINT-MAPPING>")

        parser.readBlueprintMapping(element, mapping)

        assert mapping.getBlueprintRef() is None
        assert mapping.getDerivedObjectRef() is None

    def test_read_dispatch_through_set(self, parser):
        """Test that readBlueprintMappingSet dispatches BLUEPRINT-MAPPING to readBlueprintMapping."""
        AUTOSAR.getInstance().new()
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        bms = ar_root.createBlueprintMappingSet("MySet")
        element = ET.fromstring(
            f"""<BLUEPRINT-MAPPING-SET xmlns='{NS}'>
                <SHORT-NAME>MySet</SHORT-NAME>
                <BLUEPRINT-MAPS>
                    <BLUEPRINT-MAPPING>
                        <BLUEPRINT-REF DEST="ECUC-MODULE-DEF">/Pkg/Blueprint</BLUEPRINT-REF>
                        <DERIVED-OBJECT-REF DEST="COMPU-METHOD">/Pkg/Derived</DERIVED-OBJECT-REF>
                    </BLUEPRINT-MAPPING>
                </BLUEPRINT-MAPS>
            </BLUEPRINT-MAPPING-SET>"""
        )

        parser.readBlueprintMappingSet(element, bms)

        maps = bms.getBlueprintMaps()
        assert len(maps) == 1
        assert isinstance(maps[0], BlueprintMapping)
        assert maps[0].getBlueprintRef().getValue() == "/Pkg/Blueprint"
        assert maps[0].getDerivedObjectRef().getValue() == "/Pkg/Derived"

    def test_round_trip_with_refs(self):
        """Write a set holding a BlueprintMapping with both refs, reparse, assert the values survive."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.writer.arxml_writer import ARXMLWriter

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

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            bms_2 = document_2.getARPackages()[0].getBlueprintMappingSets()[0]
            maps = bms_2.getBlueprintMaps()
            assert len(maps) == 1
            assert isinstance(maps[0], BlueprintMapping)
            assert maps[0].getBlueprintRef().getDest() == "ECUC-MODULE-DEF"
            assert maps[0].getBlueprintRef().getValue() == "/Pkg/Blueprint"
            assert maps[0].getDerivedObjectRef().getDest() == "COMPU-METHOD"
            assert maps[0].getDerivedObjectRef().getValue() == "/Pkg/Derived"
        finally:
            os.remove(file_path)
