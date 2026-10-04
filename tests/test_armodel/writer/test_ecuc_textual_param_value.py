"""Reader/writer round-trip tests for EcucTextualParamValue (Table 2.50, XSD group ECUC-TEXTUAL-PARAM-VALUE).

The single own attribute `value` is a 0..1 VerbatimString serialized as the VALUE element
(type AR:VERBATIM-STRING). Table 2.50 has no variationPoint row, so no VARIATION-POINT
element may be emitted (Rule 0015).
"""

import inspect
import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucTextualParamValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    VerbatimString,
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


class TestEcucTextualParamValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """DEFINITION-REF, INDEX, ANNOTATION, IS-AUTO-VALUE and the VerbatimString VALUE survive a write/read cycle."""
        param_value = EcucTextualParamValue()
        param_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/RteGeneration/RteGenerationMode").setDest("ECUC-ENUMERATION-PARAM-DEF"))
        param_value.setIndex(_make_index(1))
        param_value.addAnnotation(Annotation())
        param_value.setIsAutoValue(_make_boolean(False))
        param_value.setValue(VerbatimString().setValue("  CompatibilityMode  "))

        parent = ET.Element("PARENT")
        writer.writeEcucTextualParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-TEXTUAL-PARAM-VALUE" in inner
        assert "<VALUE" in inner
        assert inner.index("<DEFINITION-REF") < inner.index("<VALUE")
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucTextualParamValue()
        parser.readEcucTextualParamValue(_ns_wrap(parent), reloaded)
        assert isinstance(reloaded, EcucTextualParamValue)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Rte/RteGeneration/RteGenerationMode"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 1
        assert len(reloaded.getAnnotations()) == 1
        assert reloaded.getIsAutoValue() is not None
        assert reloaded.getIsAutoValue().getValue() is False
        assert isinstance(reloaded.getValue(), VerbatimString)
        assert reloaded.getValue().getValue() == "  CompatibilityMode  "

    def test_minimal_content_round_trip(self, writer, parser):
        """A textual parameter value without any content emits no VALUE element and reloads empty."""
        param_value = EcucTextualParamValue()

        parent = ET.Element("PARENT")
        writer.writeEcucTextualParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-TEXTUAL-PARAM-VALUE" in inner
        assert "<VALUE" not in inner
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucTextualParamValue()
        parser.readEcucTextualParamValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None
        assert reloaded.getValue() is None

    def test_spec_typed_leaf_helper_pair(self):
        """Reader and writer must use the matched VerbatimString leaf pair (Rule 0013.2)."""
        assert "getChildElementOptionalVerbatimString" in inspect.getsource(ARXMLParser.readEcucTextualParamValue)
        assert "setChildElementOptionalVerbatimString" in inspect.getsource(ARXMLWriter.writeEcucTextualParamValue)
        assert "setChildElementOptionalLiteral(" not in inspect.getsource(ARXMLWriter.writeEcucTextualParamValue)


if __name__ == "__main__":
    pytest.main([__file__])
