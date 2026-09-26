"""Parser tests for SwDataDependency / CompuGenericMath (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Tables 5.58 and 5.60, p.374).

XML element order per XSD group SW-DATA-DEPENDENCY (AUTOSAR_00052.xsd):
SW-DATA-DEPENDENCY-FORMULA (with LEVEL attribute, mixed text, S/T attributes), SW-DATA-DEPENDENCY-ARGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, PrimitiveIdentifier, String
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import CompuGenericMath
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _conditional_element(inner):
    xml = "<SW-DATA-DEF-PROPS-CONDITIONAL xmlns='%s'>%s</SW-DATA-DEF-PROPS-CONDITIONAL>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadSwDataDependency:
    def test_read_formula_level_type_and_text(self):
        element = _conditional_element("<SW-DATA-DEPENDENCY>" "<SW-DATA-DEPENDENCY-FORMULA LEVEL='INFORMAL'>X1+X2</SW-DATA-DEPENDENCY-FORMULA>" "</SW-DATA-DEPENDENCY>")
        props = SwDataDefProps()
        ARXMLParser().readSwDataDependency(element, props)

        dependency = props.getSwDataDependency()
        assert dependency is not None
        formula = dependency.getSwDataDependencyFormula()
        assert isinstance(formula, CompuGenericMath)
        assert isinstance(formula.getLevel(), PrimitiveIdentifier)
        assert formula.getLevel().getValue() == "INFORMAL"
        assert formula.getMixedString() == "X1+X2"

    def test_read_formula_without_level(self):
        element = _conditional_element("<SW-DATA-DEPENDENCY>" "<SW-DATA-DEPENDENCY-FORMULA>X1+X2</SW-DATA-DEPENDENCY-FORMULA>" "</SW-DATA-DEPENDENCY>")
        props = SwDataDefProps()
        ARXMLParser().readSwDataDependency(element, props)

        formula = props.getSwDataDependency().getSwDataDependencyFormula()
        assert isinstance(formula, CompuGenericMath)
        assert formula.getLevel() is None
        assert formula.getMixedString() == "X1+X2"

    def test_read_formula_checksum_and_timestamp(self):
        element = _conditional_element(
            "<SW-DATA-DEPENDENCY>" "<SW-DATA-DEPENDENCY-FORMULA S='deadbeef' T='2024-01-01T00:00:00.000Z' LEVEL='INFORMAL'>X1+X2</SW-DATA-DEPENDENCY-FORMULA>" "</SW-DATA-DEPENDENCY>"
        )
        props = SwDataDefProps()
        ARXMLParser().readSwDataDependency(element, props)

        formula = props.getSwDataDependency().getSwDataDependencyFormula()
        assert isinstance(formula.getChecksum(), String)
        assert formula.getChecksum().getValue() == "deadbeef"
        assert isinstance(formula.getTimestamp(), DateTime)
        assert formula.getTimestamp().getValue() == "2024-01-01T00:00:00.000Z"

    def test_read_empty_sw_data_dependency(self):
        element = _conditional_element("<SW-DATA-DEPENDENCY></SW-DATA-DEPENDENCY>")
        props = SwDataDefProps()
        ARXMLParser().readSwDataDependency(element, props)

        dependency = props.getSwDataDependency()
        assert dependency is not None
        assert dependency.getSwDataDependencyFormula() is None
        assert dependency.getSwDataDependencyArgs() is None

    def test_read_absent_sw_data_dependency(self):
        element = _conditional_element("")
        props = SwDataDefProps()
        ARXMLParser().readSwDataDependency(element, props)

        assert props.getSwDataDependency() is None
