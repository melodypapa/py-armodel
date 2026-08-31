"""
Tests for parsing BLUEPRINT-MAPPING-SET elements (BlueprintMappingSet, Table 3.1).

Round-trip counterpart: tests/test_armodel/writer/test_blueprint_mapping_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortInterfaceBlueprint import (
    PortInterfaceBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintMapping import (
    BlueprintMapping,
    BlueprintMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
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


def _make_blueprint_mapping_set() -> BlueprintMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createBlueprintMappingSet("MySet")


class TestReadBlueprintMappingSet:
    """
    Test readBlueprintMappingSet (BlueprintMappingSet.blueprintMap, Table 3.1).
    """

    def test_read_blueprint_maps(self, parser):
        """Test that BLUEPRINT-MAPS/BLUEPRINT-MAPPING populates the blueprintMaps list."""
        bms = _make_blueprint_mapping_set()
        element = ET.fromstring(
            f"""<BLUEPRINT-MAPPING-SET xmlns='{NS}'>
                <SHORT-NAME>MySet</SHORT-NAME>
                <BLUEPRINT-MAPS>
                    <BLUEPRINT-MAPPING></BLUEPRINT-MAPPING>
                </BLUEPRINT-MAPS>
            </BLUEPRINT-MAPPING-SET>"""
        )

        parser.readBlueprintMappingSet(element, bms)

        maps = bms.getBlueprintMaps()
        assert len(maps) == 1
        assert isinstance(maps[0], BlueprintMapping)
        assert isinstance(maps[0], AtpBlueprintMapping)

    def test_read_empty_blueprint_maps(self, parser):
        """Test that an absent BLUEPRINT-MAPS wrapper leaves the list empty."""
        bms = _make_blueprint_mapping_set()
        element = ET.fromstring(
            f"""<BLUEPRINT-MAPPING-SET xmlns='{NS}'>
                <SHORT-NAME>MySet</SHORT-NAME>
            </BLUEPRINT-MAPPING-SET>"""
        )

        parser.readBlueprintMappingSet(element, bms)

        assert bms.getBlueprintMaps() == []

    def test_read_port_interface_blueprint_mapping(self, parser):
        """Test that BLUEPRINT-MAPS/PORT-INTERFACE-BLUEPRINT-MAPPING populates a PortInterfaceBlueprintMapping with both refs."""
        bms = _make_blueprint_mapping_set()
        element = ET.fromstring(
            f"""<BLUEPRINT-MAPPING-SET xmlns='{NS}'>
                <SHORT-NAME>MySet</SHORT-NAME>
                <BLUEPRINT-MAPS>
                    <PORT-INTERFACE-BLUEPRINT-MAPPING>
                        <PORT-INTERFACE-BLUEPRINT-REF DEST="PORT-INTERFACE">/Pkg/BlueprintIf</PORT-INTERFACE-BLUEPRINT-REF>
                        <DERIVED-PORT-INTERFACE-REF DEST="PORT-INTERFACE">/Pkg/DerivedIf</DERIVED-PORT-INTERFACE-REF>
                    </PORT-INTERFACE-BLUEPRINT-MAPPING>
                </BLUEPRINT-MAPS>
            </BLUEPRINT-MAPPING-SET>"""
        )

        parser.readBlueprintMappingSet(element, bms)

        maps = bms.getBlueprintMaps()
        assert len(maps) == 1
        assert isinstance(maps[0], PortInterfaceBlueprintMapping)
        assert isinstance(maps[0], AtpBlueprintMapping)
        ref = maps[0].getPortInterfaceBlueprintRef()
        assert ref is not None
        assert ref.getDest() == "PORT-INTERFACE"
        assert ref.getValue() == "/Pkg/BlueprintIf"
        derived = maps[0].getDerivedPortInterfaceRef()
        assert derived is not None
        assert derived.getDest() == "PORT-INTERFACE"
        assert derived.getValue() == "/Pkg/DerivedIf"

    def test_round_trip(self):
        """Write a BlueprintMappingSet, reparse, and assert the blueprintMap survives."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        bms = ar_root.createBlueprintMappingSet("MySet")
        bms.addBlueprintMap(BlueprintMapping())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            bms_2 = document_2.getARPackages()[0].getBlueprintMappingSets()[0]
            assert bms_2.getShortName() == "MySet"
            assert len(bms_2.getBlueprintMaps()) == 1
            assert isinstance(bms_2.getBlueprintMaps()[0], BlueprintMapping)
        finally:
            os.remove(file_path)

    def test_round_trip_with_port_interface_blueprint_mapping(self):
        """Write a set holding a PortInterfaceBlueprintMapping, reparse, assert the refs survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        bms = ar_root.createBlueprintMappingSet("MySet")

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

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            bms_2 = document_2.getARPackages()[0].getBlueprintMappingSets()[0]
            maps = bms_2.getBlueprintMaps()
            assert len(maps) == 1
            assert isinstance(maps[0], PortInterfaceBlueprintMapping)
            assert maps[0].getPortInterfaceBlueprintRef().getValue() == "/Pkg/BlueprintIf"
            assert maps[0].getDerivedPortInterfaceRef().getValue() == "/Pkg/DerivedIf"
        finally:
            os.remove(file_path)
