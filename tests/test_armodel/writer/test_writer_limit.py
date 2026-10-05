"""Writer tests for Limit (Swc TPS Table 5.86, p.408).

setChildLimitElement emits the consuming element (LOWER-LIMIT, UPPER-LIMIT, ...) with
the limit value as element text and the INTERVAL-TYPE attribute carrying the UPPERCASE
XSD wire token (AR:INTERVAL-TYPE-ENUM--SIMPLE) encoded from the camelCase
IntervalTypeEnum member via INTERVAL_TYPE_XML_MAP. The full-document round-trip rides a
DataConstr -> DataConstrRule -> PhysConstrs carrier (XSD-validated save).
"""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import IntervalTypeEnum, Limit
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import DataConstrRule, PhysConstrs
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_lower_limit() -> Limit:
    limit = Limit()
    limit.setValue("0")
    limit.setIntervalType(IntervalTypeEnum().setValue(IntervalTypeEnum.CLOSED))
    return limit


class TestWriteLimit:
    def test_write_interval_type_token(self):
        parent_element = ET.Element("PARENT")
        ARXMLWriter().setChildLimitElement(parent_element, "LOWER-LIMIT", _build_lower_limit())

        limit_element = parent_element.find("LOWER-LIMIT")
        assert limit_element is not None
        assert limit_element.attrib["INTERVAL-TYPE"] == "CLOSED"
        assert limit_element.text == "0"

    def test_write_without_interval_type_omits_attribute(self):
        parent_element = ET.Element("PARENT")
        limit = Limit()
        limit.setValue("INF")
        ARXMLWriter().setChildLimitElement(parent_element, "UPPER-LIMIT", limit)

        limit_element = parent_element.find("UPPER-LIMIT")
        assert limit_element is not None
        assert "INTERVAL-TYPE" not in limit_element.attrib
        assert limit_element.text == "INF"


class TestLimitRoundTrip:
    def test_round_trip_through_data_constr(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Limits")
        constr = pkg.createDataConstr("DataConstr")
        rule = DataConstrRule()
        phys_constrs = PhysConstrs()
        phys_constrs.setLowerLimit(_build_lower_limit())
        upper = Limit()
        upper.setValue("INF")
        phys_constrs.setUpperLimit(upper)
        rule.setPhysConstrs(phys_constrs)
        constr.addDataConstrRule(rule)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            xml = open(file_path, encoding="utf-8").read()
            assert 'INTERVAL-TYPE="CLOSED"' in xml

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            constr_2 = document_2.getARPackages()[0].getDataConstrs()[0]
            rule_2 = constr_2.getDataConstrRules()[0]
            phys_constrs_2 = rule_2.getPhysConstrs()
            lower_2 = phys_constrs_2.getLowerLimit()
            assert isinstance(lower_2, Limit)
            assert lower_2.getValue() == "0"
            assert isinstance(lower_2.getIntervalType(), IntervalTypeEnum)
            assert lower_2.getIntervalType().getValue() == "closed"
            upper_2 = phys_constrs_2.getUpperLimit()
            assert isinstance(upper_2, Limit)
            assert upper_2.getValue() == "INF"
            assert upper_2.getIntervalType() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
