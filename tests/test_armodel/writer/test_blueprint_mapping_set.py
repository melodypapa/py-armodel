"""
Tests for writing BLUEPRINT-MAPPING-SET elements (BlueprintMappingSet, Table 3.1).

Round-trip counterpart: tests/test_armodel/parser/test_blueprint_mapping_set.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortInterfaceBlueprint import (
    PortInterfaceBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMapping,
    BlueprintMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteBlueprintMappingSet:
    """
    Test writeBlueprintMappingSet (BlueprintMappingSet.blueprintMap, Table 3.1).
    """

    def test_write_blueprint_maps(self):
        """Test that blueprintMaps are written as BLUEPRINT-MAPS/BLUEPRINT-MAPPING."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        bms = BlueprintMappingSet(None, "MySet")
        bms.addBlueprintMap(BlueprintMapping())

        writer.writeBlueprintMappingSet(element, bms)

        bms_tag = element.find("BLUEPRINT-MAPPING-SET")
        assert bms_tag is not None
        maps_tag = bms_tag.find("BLUEPRINT-MAPS")
        assert maps_tag is not None
        assert maps_tag.find("BLUEPRINT-MAPPING") is not None

    def test_write_empty_blueprint_maps(self):
        """Test that an empty blueprintMaps list writes no BLUEPRINT-MAPS wrapper."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        bms = BlueprintMappingSet(None, "MySet")
        writer.writeBlueprintMappingSet(element, bms)

        bms_tag = element.find("BLUEPRINT-MAPPING-SET")
        assert bms_tag is not None
        assert bms_tag.find("BLUEPRINT-MAPS") is None

    def test_write_port_interface_blueprint_mapping(self):
        """Test that a PortInterfaceBlueprintMapping writes as BLUEPRINT-MAPS/PORT-INTERFACE-BLUEPRINT-MAPPING with both refs."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        bms = BlueprintMappingSet(None, "MySet")
        pibm = PortInterfaceBlueprintMapping()
        blueprint_ref = RefType()
        blueprint_ref.setDest("PORT-INTERFACE")
        blueprint_ref.setValue("/Pkg/BlueprintIf")
        pibm.setPortInterfaceBlueprintRef(blueprint_ref)
        derived_ref = RefType()
        derived_ref.setDest("PORT-INTERFACE")
        derived_ref.setValue("/Pkg/DerivedIf")
        pibm.setDerivedPortInterfaceRef(derived_ref)
        bms.addBlueprintMap(pibm)

        writer.writeBlueprintMappingSet(element, bms)

        bms_tag = element.find("BLUEPRINT-MAPPING-SET")
        assert bms_tag is not None
        maps_tag = bms_tag.find("BLUEPRINT-MAPS")
        assert maps_tag is not None
        pibm_tag = maps_tag.find("PORT-INTERFACE-BLUEPRINT-MAPPING")
        assert pibm_tag is not None
        ref_tag = pibm_tag.find("PORT-INTERFACE-BLUEPRINT-REF")
        assert ref_tag is not None
        assert ref_tag.attrib["DEST"] == "PORT-INTERFACE"
        assert ref_tag.text == "/Pkg/BlueprintIf"
        derived_tag = pibm_tag.find("DERIVED-PORT-INTERFACE-REF")
        assert derived_tag is not None
        assert derived_tag.attrib["DEST"] == "PORT-INTERFACE"
        assert derived_tag.text == "/Pkg/DerivedIf"

    def test_write_port_prototype_blueprint_mapping(self):
        """Test that a PortPrototypeBlueprintMapping writes as BLUEPRINT-MAPS/PORT-PROTOTYPE-BLUEPRINT-MAPPING with both refs."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        bms = BlueprintMappingSet(None, "MySet")
        ppbm = PortPrototypeBlueprintMapping()
        blueprint_ref = RefType()
        blueprint_ref.setDest("PORT-PROTOTYPE-BLUEPRINT")
        blueprint_ref.setValue("/Pkg/BlueprintPort")
        ppbm.setPortPrototypeBlueprintRef(blueprint_ref)
        derived_ref = RefType()
        derived_ref.setDest("P-PORT-PROTOTYPE")
        derived_ref.setValue("/Pkg/Swc/DerivedPort")
        ppbm.setDerivedPortPrototypeRef(derived_ref)
        bms.addBlueprintMap(ppbm)

        writer.writeBlueprintMappingSet(element, bms)

        bms_tag = element.find("BLUEPRINT-MAPPING-SET")
        assert bms_tag is not None
        maps_tag = bms_tag.find("BLUEPRINT-MAPS")
        assert maps_tag is not None
        ppbm_tag = maps_tag.find("PORT-PROTOTYPE-BLUEPRINT-MAPPING")
        assert ppbm_tag is not None
        ref_tag = ppbm_tag.find("PORT-PROTOTYPE-BLUEPRINT-REF")
        assert ref_tag is not None
        assert ref_tag.attrib["DEST"] == "PORT-PROTOTYPE-BLUEPRINT"
        assert ref_tag.text == "/Pkg/BlueprintPort"
        derived_tag = ppbm_tag.find("DERIVED-PORT-PROTOTYPE-REF")
        assert derived_tag is not None
        assert derived_tag.attrib["DEST"] == "P-PORT-PROTOTYPE"
        assert derived_tag.text == "/Pkg/Swc/DerivedPort"

    def test_round_trip(self):
        """Build a model, write it, reparse, and assert the blueprintMap survives."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        bms = ar_root.createBlueprintMappingSet("MySet")
        bms.addBlueprintMap(BlueprintMapping())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            from armodel.parser.arxml_parser import ARXMLParser

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            bms_2 = document_2.getARPackages()[0].getBlueprintMappingSets()[0]
            assert bms_2.getShortName() == "MySet"
            assert len(bms_2.getBlueprintMaps()) == 1
            assert isinstance(bms_2.getBlueprintMaps()[0], BlueprintMapping)
        finally:
            os.remove(file_path)
