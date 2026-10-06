"""Writer round-trip tests for ReferenceValueSpecification (Swc TPS Table 5.115, p.437).

The element serializes as REFERENCE-VALUE-SPECIFICATION with the single ref child
REFERENCE-VALUE-REF (DEST = DATA-PROTOTYPE per the XSD group REFERENCE-VALUE-SPECIFICATION,
AUTOSAR_00052.xsd L96564), after the inherited ValueSpecification level (SHORT-LABEL,
AR:AR-OBJECT) written by writeValueSpecification. The full-document round-trip rides
ARPackage.createConstantSpecification (XSD-validated save).
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ReferenceValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_reference_value_specification() -> ReferenceValueSpecification:
    value_spec = ReferenceValueSpecification()
    ref = RefType()
    ref.setDest("DATA-PROTOTYPE")
    ref.setValue("/DataTypes/PointerTarget")
    value_spec.setReferenceValueRef(ref)
    return value_spec


class TestWriteReferenceValueSpecification:
    def test_write_element_and_ref(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeReferenceValueSpecification(parent, _build_reference_value_specification())

        tag = parent.find("REFERENCE-VALUE-SPECIFICATION")
        assert tag is not None
        ref_tag = tag.find("REFERENCE-VALUE-REF")
        assert ref_tag is not None
        assert ref_tag.get("DEST") == "DATA-PROTOTYPE"
        assert ref_tag.text == "/DataTypes/PointerTarget"

    def test_write_empty_omits_ref(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeReferenceValueSpecification(parent, ReferenceValueSpecification())

        tag = parent.find("REFERENCE-VALUE-SPECIFICATION")
        assert tag is not None
        assert tag.find("REFERENCE-VALUE-REF") is None


class TestReferenceValueSpecificationRoundTrip:
    def test_round_trip_full_field_values(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Consts")
        constant = pkg.createConstantSpecification("C1")
        constant.setValueSpec(_build_reference_value_specification())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constant_2 = document_2.getARPackages()[0].getConstantSpecifications()[0]
            value_spec_2 = constant_2.getValueSpec()
            assert isinstance(value_spec_2, ReferenceValueSpecification)
            ref_2 = value_spec_2.getReferenceValueRef()
            assert ref_2 is not None
            assert ref_2.getDest() == "DATA-PROTOTYPE"
            assert ref_2.getValue() == "/DataTypes/PointerTarget"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Consts")
        constant = pkg.createConstantSpecification("C2")
        constant.setValueSpec(ReferenceValueSpecification())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constant_2 = document_2.getARPackages()[0].getConstantSpecifications()[0]
            value_spec_2 = constant_2.getValueSpec()
            assert isinstance(value_spec_2, ReferenceValueSpecification)
            assert value_spec_2.getReferenceValueRef() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
