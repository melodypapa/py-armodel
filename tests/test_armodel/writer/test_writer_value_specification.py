"""Writer round-trip tests for ValueSpecification (Swc TPS Table 5.109, p.433).

ValueSpecification is abstract: its own XML group (SHORT-LABEL, then VARIATION-POINT
per the XSD group VALUE-SPECIFICATION, AUTOSAR_00052.xsd L129398) is serialized by the
reusable readValueSpecification/writeValueSpecification helpers that every concrete
subclass calls. The full-document round-trip rides ARPackage.createConstantSpecification
(XSD-validated save) with a concrete NumericalValueSpecification carrying the base-owned
shortLabel (0..1 Identifier).
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import ConstantSpecification, NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, Numerical
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_document():
    document = AUTOSAR.getInstance()
    document.clear()
    document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
    pkg = document.createARPackage("Consts")
    constant = pkg.createConstantSpecification("C1")

    value_spec = NumericalValueSpecification()
    value_spec.setShortLabel(Identifier().setValue("field1"))
    value_spec.setValue(Numerical().setValue("42"))
    constant.setValueSpec(value_spec)
    return document, constant


class TestValueSpecificationRoundTrip:
    def test_round_trip_short_label_and_subclass_field_values(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document, _constant = _build_document()

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constant_2 = document_2.getARPackages()[0].getConstantSpecifications()[0]
            value_spec_2 = constant_2.getValueSpec()
            assert isinstance(value_spec_2, NumericalValueSpecification)
            assert value_spec_2.getShortLabel() is not None
            assert value_spec_2.getShortLabel().getValue() == "field1"
            assert value_spec_2.getValue() is not None
            assert value_spec_2.getValue().getValue() == 42
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_absent_value_specification(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Consts")
        pkg.createConstantSpecification("C0")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constant_2 = document_2.getARPackages()[0].getConstantSpecifications()[0]
            assert isinstance(constant_2, ConstantSpecification)
            assert constant_2.getValueSpec() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
