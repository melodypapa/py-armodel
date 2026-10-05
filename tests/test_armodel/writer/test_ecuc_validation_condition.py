"""Writer/reader round-trip tests for EcucValidationCondition (ECUC-VALIDATION-CONDITION)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucConditionFormula,
    EcucParamConfContainerDef,
    EcucQueryExpression,
    EcucValidationCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestEcucValidationConditionRoundTrip:
    def test_full_validation_condition_round_trip(self, writer, parser):
        validation_condition = EcucValidationCondition(None, "VC1")
        query = validation_condition.createEcucQuery("GetSpeedLimit")
        expr = EcucQueryExpression()
        expr.setConfigElementDefGlobalRef(_ref("/EcucDefs/Mod/Param", "ECUC-INTEGER-PARAM-DEF"))
        query.setEcucQueryExpression(expr)
        formula = EcucConditionFormula()
        formula.setEcucQueryStringRef(_ref("/EcucDefs/Mod/Query2", "ECUC-QUERY"))
        validation_condition.setValidationFormula(formula)

        parent = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        vc_element = ET.SubElement(parent, "ECUC-VALIDATION-CONDITION")
        writer.writeEcucValidationCondition(vc_element, validation_condition)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-VALIDATION-CONDITION>" in inner
        assert "<SHORT-NAME>VC1</SHORT-NAME>" in inner
        assert "<ECUC-QUERYS>" in inner
        assert "<VALIDATION-FORMULA>" in inner
        assert inner.index("<ECUC-QUERYS>") < inner.index("<VALIDATION-FORMULA>")

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        reloaded = parser.readEcucValidationCondition(root[0][0])
        assert reloaded is not None
        assert reloaded.getShortName() == "VC1"
        queries = reloaded.getEcucQueries()
        assert len(queries) == 1
        assert queries[0].getShortName() == "GetSpeedLimit"
        expr_reloaded = queries[0].getEcucQueryExpression()
        assert expr_reloaded is not None
        assert expr_reloaded.getConfigElementDefGlobalRef() is not None
        assert expr_reloaded.getConfigElementDefGlobalRef().getValue() == "/EcucDefs/Mod/Param"
        reloaded_formula = reloaded.getValidationFormula()
        assert reloaded_formula is not None
        assert reloaded_formula.getEcucQueryStringRef() is not None
        assert reloaded_formula.getEcucQueryStringRef().getValue() == "/EcucDefs/Mod/Query2"
        assert reloaded_formula.getEcucQueryStringRef().getDest() == "ECUC-QUERY"

    def test_aggregated_validation_conditions_round_trip(self, writer, parser):
        container = EcucParamConfContainerDef(None, "Ct")
        validation_condition = EcucValidationCondition(container, "VC2")
        query = validation_condition.createEcucQuery("GetAngle")
        expr = EcucQueryExpression()
        expr.setConfigElementDefLocalRef(_ref("/EcucDefs/Mod/Local", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        query.setEcucQueryExpression(expr)
        container.addEcucValidationCond(validation_condition)

        parent = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        writer.writeEcucValidationConditions(parent, container.getEcucValidationConds())
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-VALIDATION-CONDS>" in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        reloaded_container = EcucParamConfContainerDef(None, "Ct")
        parser.readEcucValidationConditions(root[0], reloaded_container)
        conds = reloaded_container.getEcucValidationConds()
        assert len(conds) == 1
        assert conds[0].getShortName() == "VC2"
        queries = conds[0].getEcucQueries()
        assert len(queries) == 1
        assert queries[0].getShortName() == "GetAngle"
        assert queries[0].getEcucQueryExpression().getConfigElementDefLocalRef().getValue() == "/EcucDefs/Mod/Local"
        assert conds[0].getValidationFormula() is None

    def test_empty_validation_conditions_no_wrapper(self, writer):
        container = EcucParamConfContainerDef(None, "Ct")
        parent = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        writer.writeEcucValidationConditions(parent, container.getEcucValidationConds())
        assert len(parent) == 0
