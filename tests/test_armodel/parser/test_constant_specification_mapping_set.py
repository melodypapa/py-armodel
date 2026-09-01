"""
Tests for parsing CONSTANT-SPECIFICATION-MAPPING-SET elements (ConstantSpecificationMappingSet, Table 5.119).

Round-trip counterpart: tests/test_armodel/writer/test_constant_specification_mapping_set.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ConstantSpecificationMapping,
    ConstantSpecificationMappingSet,
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


def _make_constant_specification_mapping_set() -> ConstantSpecificationMappingSet:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createConstantSpecificationMappingSet("MySet")


class TestReadConstantSpecificationMappingSet:
    """
    Test readConstantSpecificationMappingSet (ConstantSpecificationMappingSet.mapping, Table 5.119).
    """

    def test_read_mappings(self, parser):
        """Test that MAPPINGS/CONSTANT-SPECIFICATION-MAPPING populates the mappings list with both refs."""
        csms = _make_constant_specification_mapping_set()
        element = ET.fromstring(
            f"""<CONSTANT-SPECIFICATION-MAPPING-SET xmlns='{NS}'>
                <SHORT-NAME>MySet</SHORT-NAME>
                <MAPPINGS>
                    <CONSTANT-SPECIFICATION-MAPPING>
                        <APPL-CONSTANT-REF DEST="CONSTANT-SPECIFICATION">/Pkg/ApplConst</APPL-CONSTANT-REF>
                        <IMPL-CONSTANT-REF DEST="CONSTANT-SPECIFICATION">/Pkg/ImplConst</IMPL-CONSTANT-REF>
                    </CONSTANT-SPECIFICATION-MAPPING>
                </MAPPINGS>
            </CONSTANT-SPECIFICATION-MAPPING-SET>"""
        )

        parser.readConstantSpecificationMappingSet(element, csms)

        mappings = csms.getMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], ConstantSpecificationMapping)
        appl_ref = mappings[0].getApplConstantRef()
        assert appl_ref is not None
        assert appl_ref.getDest() == "CONSTANT-SPECIFICATION"
        assert appl_ref.getValue() == "/Pkg/ApplConst"
        impl_ref = mappings[0].getImplConstantRef()
        assert impl_ref is not None
        assert impl_ref.getDest() == "CONSTANT-SPECIFICATION"
        assert impl_ref.getValue() == "/Pkg/ImplConst"

    def test_read_empty_mappings(self, parser):
        """Test that an absent MAPPINGS wrapper leaves the list empty."""
        csms = _make_constant_specification_mapping_set()
        element = ET.fromstring(
            f"""<CONSTANT-SPECIFICATION-MAPPING-SET xmlns='{NS}'>
                <SHORT-NAME>MySet</SHORT-NAME>
            </CONSTANT-SPECIFICATION-MAPPING-SET>"""
        )

        parser.readConstantSpecificationMappingSet(element, csms)

        assert csms.getMappings() == []

    def test_round_trip(self):
        """Write a ConstantSpecificationMappingSet, reparse, and assert the mapping refs survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        csms = ar_root.createConstantSpecificationMappingSet("MySet")

        mapping = ConstantSpecificationMapping()
        appl_ref = RefType()
        appl_ref.setDest("CONSTANT-SPECIFICATION")
        appl_ref.setValue("/Pkg/ApplConst")
        mapping.setApplConstantRef(appl_ref)
        impl_ref = RefType()
        impl_ref.setDest("CONSTANT-SPECIFICATION")
        impl_ref.setValue("/Pkg/ImplConst")
        mapping.setImplConstantRef(impl_ref)
        csms.addMapping(mapping)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            from armodel.writer.arxml_writer import ARXMLWriter

            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            csms_2 = document_2.getARPackages()[0].getConstantSpecificationMappingSets()[0]
            assert csms_2.getShortName() == "MySet"
            mappings = csms_2.getMappings()
            assert len(mappings) == 1
            assert isinstance(mappings[0], ConstantSpecificationMapping)
            assert mappings[0].getApplConstantRef().getValue() == "/Pkg/ApplConst"
            assert mappings[0].getApplConstantRef().getDest() == "CONSTANT-SPECIFICATION"
            assert mappings[0].getImplConstantRef().getValue() == "/Pkg/ImplConst"
            assert mappings[0].getImplConstantRef().getDest() == "CONSTANT-SPECIFICATION"
        finally:
            os.remove(file_path)
