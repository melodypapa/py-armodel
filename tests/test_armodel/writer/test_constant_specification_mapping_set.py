"""
Tests for writing CONSTANT-SPECIFICATION-MAPPING-SET elements (ConstantSpecificationMappingSet, Table 5.119).

Round-trip counterpart: tests/test_armodel/parser/test_constant_specification_mapping_set.py
"""

import logging
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ConstantSpecificationMapping,
    ConstantSpecificationMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteConstantSpecificationMappingSet:
    """
    Test writeConstantSpecificationMappingSet (ConstantSpecificationMappingSet.mapping, Table 5.119).
    """

    def test_write_mappings(self):
        """Test that mappings are written as MAPPINGS/CONSTANT-SPECIFICATION-MAPPING with both refs."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        csms = ConstantSpecificationMappingSet(None, "MySet")
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

        writer.writeConstantSpecificationMappingSet(element, csms)

        csms_tag = element.find("CONSTANT-SPECIFICATION-MAPPING-SET")
        assert csms_tag is not None
        mappings_tag = csms_tag.find("MAPPINGS")
        assert mappings_tag is not None
        mapping_tag = mappings_tag.find("CONSTANT-SPECIFICATION-MAPPING")
        assert mapping_tag is not None
        appl_ref_tag = mapping_tag.find("APPL-CONSTANT-REF")
        assert appl_ref_tag is not None
        assert appl_ref_tag.get("DEST") == "CONSTANT-SPECIFICATION"
        assert appl_ref_tag.text == "/Pkg/ApplConst"
        impl_ref_tag = mapping_tag.find("IMPL-CONSTANT-REF")
        assert impl_ref_tag is not None
        assert impl_ref_tag.get("DEST") == "CONSTANT-SPECIFICATION"
        assert impl_ref_tag.text == "/Pkg/ImplConst"

    def test_write_empty_mappings(self):
        """Test that an empty mappings list writes no MAPPINGS wrapper."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        csms = ConstantSpecificationMappingSet(None, "MySet")
        writer.writeConstantSpecificationMappingSet(element, csms)

        csms_tag = element.find("CONSTANT-SPECIFICATION-MAPPING-SET")
        assert csms_tag is not None
        assert csms_tag.find("MAPPINGS") is None
