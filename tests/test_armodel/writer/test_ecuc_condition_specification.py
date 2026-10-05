"""Writer/reader round-trip tests for EcucConditionSpecification (ECUC-COND)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucConditionFormula,
    EcucConditionSpecification,
    EcucQueryExpression,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LPlainText
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguagePlainText
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


class TestEcucConditionSpecificationRoundTrip:
    def test_full_condition_specification_round_trip(self, writer, parser):
        cond = EcucConditionSpecification()
        formula = EcucConditionFormula()
        formula.setEcucQueryRef(_ref("/EcucDefs/Mod/Query", "ECUC-QUERY"))
        cond.setConditionFormula(formula)
        query = cond.createEcucQuery("GetTTCanEnabled")
        expr = EcucQueryExpression()
        expr.setConfigElementDefLocalRef(_ref("/EcucDefs/Mod/CanIfPrivateCfg/CanIfSupportTTCAN", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        query.setEcucQueryExpression(expr)
        informal = MlFormula()
        tex_math = MultiLanguagePlainText()
        l10 = LPlainText()
        l10.setValue("value > 0")
        tex_math.addL10(l10)
        informal.setTexMath(tex_math)
        cond.setInformalFormula(informal)

        parent = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        writer.writeEcucConditionSpecification(parent, cond)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-COND>" in inner
        assert "<CONDITION-FORMULA>" in inner
        assert "<ECUC-QUERYS>" in inner
        assert "<ECUC-QUERY>" in inner
        assert "<INFORMAL-FORMULA>" in inner
        assert inner.index("<CONDITION-FORMULA>") < inner.index("<ECUC-QUERYS>") < inner.index("<INFORMAL-FORMULA>")

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        reloaded = parser.readEcucConditionSpecification(root[0])
        assert reloaded is not None
        reloaded_formula = reloaded.getConditionFormula()
        assert reloaded_formula is not None
        assert reloaded_formula.getEcucQueryRef() is not None
        assert reloaded_formula.getEcucQueryRef().getValue() == "/EcucDefs/Mod/Query"
        assert reloaded_formula.getEcucQueryRef().getDest() == "ECUC-QUERY"
        queries = reloaded.getEcucQueries()
        assert len(queries) == 1
        assert queries[0].getShortName() == "GetTTCanEnabled"
        expr_reloaded = queries[0].getEcucQueryExpression()
        assert expr_reloaded is not None
        assert expr_reloaded.getConfigElementDefLocalRef() is not None
        assert expr_reloaded.getConfigElementDefLocalRef().getValue() == "/EcucDefs/Mod/CanIfPrivateCfg/CanIfSupportTTCAN"
        reloaded_informal = reloaded.getInformalFormula()
        assert isinstance(reloaded_informal, MlFormula)
        assert reloaded_informal.getTexMath() is not None
        assert reloaded_informal.getTexMath().getL10s()[0].getValue() == "value > 0"

    def test_empty_queries_wrapper_not_emitted(self, writer, parser):
        cond = EcucConditionSpecification()
        cond.setConditionFormula(EcucConditionFormula())

        parent = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        writer.writeEcucConditionSpecification(parent, cond)
        cond_element = parent.find("ECUC-COND")
        assert cond_element is not None
        assert cond_element.find("ECUC-QUERYS") is None

        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        reloaded = parser.readEcucConditionSpecification(root[0])
        assert reloaded is not None
        assert reloaded.getEcucQueries() == []
        assert reloaded.getConditionFormula() is not None
        assert reloaded.getInformalFormula() is None

    def test_no_condition_no_element_emitted(self, writer):
        parent = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        writer.writeEcucConditionSpecification(parent, None)
        assert len(parent) == 0
