"""Reader/writer round-trip tests for EcucNumericalParamValue (Table 2.51, XSD group ECUC-NUMERICAL-PARAM-VALUE).

The single own attribute `value` is a 0..1 Numerical serialized as the VALUE element
(PDF type Numerical; the XSD's NUMERICAL-VALUE-VARIATION-POINT is the atpVariation
attribute-value artifact — Rule 0015, the PDF/markdown table wins). Table 2.51 has no
variationPoint row, so no VARIATION-POINT element may be emitted.
"""

import inspect
import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucNumericalParamValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Numerical,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _make_index(value):
    index = PositiveInteger()
    index.setValue(str(value))
    return index


def _make_boolean(value):
    flag = Boolean()
    flag.setValue(value)
    return flag


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


def _ns_wrap(parent):
    """Serialize the PARENT's ECUC child under the AUTOSAR namespace and return the ECUC element."""
    return ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))[0][0]


class TestEcucNumericalParamValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """DEFINITION-REF, INDEX, ANNOTATION, IS-AUTO-VALUE and the Numerical VALUE survive a write/read cycle."""
        param_value = EcucNumericalParamValue()
        param_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/RteGeneration/RteDevErrorDetect").setDest("ECUC-BOOLEAN-PARAM-DEF"))
        param_value.setIndex(_make_index(3))
        param_value.addAnnotation(Annotation())
        param_value.setIsAutoValue(_make_boolean(True))
        param_value.setValue(Numerical().setValue("74.8"))

        parent = ET.Element("PARENT")
        writer.writeEcucNumericalParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-NUMERICAL-PARAM-VALUE" in inner
        assert "<VALUE" in inner
        assert inner.index("<DEFINITION-REF") < inner.index("<VALUE")
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucNumericalParamValue()
        parser.readEcucNumericalParamValue(_ns_wrap(parent), reloaded)
        assert isinstance(reloaded, EcucNumericalParamValue)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Rte/RteGeneration/RteDevErrorDetect"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 3
        assert len(reloaded.getAnnotations()) == 1
        assert reloaded.getIsAutoValue() is not None
        assert reloaded.getIsAutoValue().getValue() is True
        assert isinstance(reloaded.getValue(), Numerical)
        assert reloaded.getValue().getValue() == 74.8

    def test_hex_text_preserved_round_trip(self, writer, parser):
        """A hex Numerical VALUE keeps its verbatim text on the write/read cycle."""
        param_value = EcucNumericalParamValue()
        param_value.setValue(Numerical().setValue("0x10"))

        parent = ET.Element("PARENT")
        writer.writeEcucNumericalParamValue(parent, param_value)
        assert "<VALUE>0x10</VALUE>" in ET.tostring(parent).decode("utf-8")

        reloaded = EcucNumericalParamValue()
        parser.readEcucNumericalParamValue(_ns_wrap(parent), reloaded)
        assert reloaded.getValue() is not None
        assert reloaded.getValue().getValue() == 16
        assert reloaded.getValue().getText() == "0x10"

    def test_minimal_content_round_trip(self, writer, parser):
        """A numerical parameter value without any content emits no VALUE element and reloads empty."""
        param_value = EcucNumericalParamValue()

        parent = ET.Element("PARENT")
        writer.writeEcucNumericalParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-NUMERICAL-PARAM-VALUE" in inner
        assert "<VALUE" not in inner
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucNumericalParamValue()
        parser.readEcucNumericalParamValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None
        assert reloaded.getValue() is None

    def test_spec_typed_leaf_helper_pair(self):
        """Reader and writer must use the matched Numerical leaf pair (Rule 0013.2)."""
        assert "getChildElementOptionalNumerical" in inspect.getsource(ARXMLParser.readEcucNumericalParamValue)
        assert "setChildElementOptionalNumerical(" in inspect.getsource(ARXMLWriter.writeEcucNumericalParamValue)


if __name__ == "__main__":
    pytest.main([__file__])
