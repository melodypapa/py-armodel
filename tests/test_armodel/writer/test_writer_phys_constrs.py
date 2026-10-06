"""Writer tests for PhysConstrs (Swc TPS Table 5.84, p.406).

setPhysConstrs emits PHYS-CONSTRS with the children in the XSD group sequence order
(AUTOSAR_00052.xsd): LOWER-LIMIT (sequenceOffset 20), UPPER-LIMIT (30), SCALE-CONSTRS
(40), MAX-GRADIENT (50), MAX-DIFF (60), MONOTONY (70), UNIT-REF (80). MONOTONY carries
the UPPERCASE XSD wire token (AR:MONOTONY-ENUM--SIMPLE) encoded from the camelCase
MonotonyEnum member via MONOTONY_XML_MAP. The full-document round-trip rides
ARPackage.createDataConstr (XSD-validated save).
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import IntervalTypeEnum, Limit, MonotonyEnum, Numerical, RefType
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstrRule, PhysConstrs, ScaleConstr
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _identifier(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

    return Identifier().setValue(value)


def _build_phys_constrs() -> PhysConstrs:
    constrs = PhysConstrs()
    lower = Limit()
    lower.setValue("0")
    lower.setIntervalType(IntervalTypeEnum().setValue(IntervalTypeEnum.CLOSED))
    constrs.setLowerLimit(lower)
    upper = Limit()
    upper.setValue("65535")
    upper.setIntervalType(IntervalTypeEnum().setValue(IntervalTypeEnum.OPEN))
    constrs.setUpperLimit(upper)
    scale = ScaleConstr()
    scale.setShortLabel(_identifier("s1"))
    scale_lower = Limit()
    scale_lower.setValue("5.0")
    scale.setLowerLimit(scale_lower)
    scale_upper = Limit()
    scale_upper.setValue("50.0")
    scale.setUpperLimit(scale_upper)
    constrs.addScaleConstr(scale)
    max_gradient = Numerical()
    max_gradient.setValue("1.5")
    constrs.setMaxGradient(max_gradient)
    max_diff = Numerical()
    max_diff.setValue("0.5")
    constrs.setMaxDiff(max_diff)
    constrs.setMonotony(MonotonyEnum().setValue(MonotonyEnum.INCREASING))
    unit_ref = RefType()
    unit_ref.setValue("/units/c")
    unit_ref.setDest("UNIT")
    constrs.setUnitRef(unit_ref)
    return constrs


class TestWritePhysConstrs:
    def test_write_element_order_matches_xsd_group(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setPhysConstrs(parent_element, _build_phys_constrs())

        constrs_element = parent_element.find("PHYS-CONSTRS")
        assert constrs_element is not None
        tags = [element.tag for element in constrs_element]
        assert tags == ["LOWER-LIMIT", "UPPER-LIMIT", "SCALE-CONSTRS", "MAX-GRADIENT", "MAX-DIFF", "MONOTONY", "UNIT-REF"]

    def test_write_monotony_token(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setPhysConstrs(parent_element, _build_phys_constrs())

        constrs_element = parent_element.find("PHYS-CONSTRS")
        assert constrs_element.find("MONOTONY").text == "INCREASING"
        assert constrs_element.find("LOWER-LIMIT").attrib["INTERVAL-TYPE"] == "CLOSED"
        assert constrs_element.find("UNIT-REF").text == "/units/c"
        assert constrs_element.find("UNIT-REF").attrib["DEST"] == "UNIT"

    def test_write_empty_omits_element(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setPhysConstrs(parent_element, None)
        assert len(parent_element) == 0


class TestPhysConstrsRoundTrip:
    def test_round_trip_full_field_values(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Constrs")
        constr = pkg.createDataConstr("DataConstr")
        rule = DataConstrRule()
        rule.setPhysConstrs(_build_phys_constrs())
        constr.addDataConstrRule(rule)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constr_2 = document_2.getARPackages()[0].getDataConstrs()[0]
            rule_2 = constr_2.getDataConstrRules()[0]
            constrs_2 = rule_2.getPhysConstrs()
            assert constrs_2 is not None
            lower_2 = constrs_2.getLowerLimit()
            assert lower_2.getValue() == "0"
            assert lower_2.getIntervalType().getValue() == "closed"
            upper_2 = constrs_2.getUpperLimit()
            assert upper_2.getValue() == "65535"
            assert upper_2.getIntervalType().getValue() == "open"
            assert constrs_2.getMaxGradient().getValue() == 1.5
            assert constrs_2.getMaxDiff().getValue() == 0.5
            assert isinstance(constrs_2.getMonotony(), MonotonyEnum)
            assert constrs_2.getMonotony().getValue() == "increasing"
            scales_2 = constrs_2.getScaleConstrs()
            assert len(scales_2) == 1
            assert scales_2[0].getShortLabel().getValue() == "s1"
            assert scales_2[0].getLowerLimit().getValue() == "5.0"
            assert scales_2[0].getUpperLimit().getValue() == "50.0"
            assert constrs_2.getUnitRef().getValue() == "/units/c"
            assert constrs_2.getUnitRef().getDest() == "UNIT"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd"
        pkg = document.createARPackage("Constrs")
        constr = pkg.createDataConstr("DataConstr")
        rule = DataConstrRule()
        rule.setPhysConstrs(PhysConstrs())
        constr.addDataConstrRule(rule)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constr_2 = document_2.getARPackages()[0].getDataConstrs()[0]
            constrs_2 = constr_2.getDataConstrRules()[0].getPhysConstrs()
            assert constrs_2 is not None
            assert constrs_2.getLowerLimit() is None
            assert constrs_2.getUpperLimit() is None
            assert constrs_2.getMaxDiff() is None
            assert constrs_2.getMaxGradient() is None
            assert constrs_2.getMonotony() is None
            assert constrs_2.getScaleConstrs() == []
            assert constrs_2.getUnitRef() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
