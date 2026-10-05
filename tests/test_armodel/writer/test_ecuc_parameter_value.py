"""Reader/writer round-trip tests for EcucParameterValue (abstract, XSD group ECUC-PARAMETER-VALUE).

EcucParameterValue has no standalone XML element: its content (DEFINITION-REF, ANNOTATION,
IS-AUTO-VALUE) is serialized inside the concrete subclasses (EcucTextualParamValue,
EcucNumericalParamValue, EcucAddInfoParamValue). Coverage therefore exercises the reusable
readEcucParameterValue / writeEcucParameterValue helpers through the concrete readers/writers
that call them. Table 2.49 has no variationPoint row, so no VARIATION-POINT element may be
emitted (Rule 0015).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucNumericalParamValue,
    EcucTextualParamValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Numerical, PositiveInteger, RefType
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


class TestEcucParameterValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """DEFINITION-REF, INDEX, ANNOTATION and IS-AUTO-VALUE survive a write/read cycle in XSD order."""
        param_value = EcucNumericalParamValue()
        param_value.setDefinitionRef(RefType().setValue("/EcucDefs/Os/OsOS/OsParam").setDest("ECUC-NUMERICAL-PARAM-VALUE"))
        param_value.setIndex(_make_index(2))
        param_value.addAnnotation(Annotation())
        param_value.setIsAutoValue(_make_boolean(True))
        param_value.setValue(Numerical().setValue("10"))

        parent = ET.Element("PARENT")
        writer.writeEcucNumericalParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-NUMERICAL-PARAM-VALUE>" in inner
        assert inner.index("<DEFINITION-REF") < inner.index("<INDEX>") < inner.index("<ANNOTATION") < inner.index("<IS-AUTO-VALUE>")
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucNumericalParamValue()
        parser.readEcucNumericalParamValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Os/OsOS/OsParam"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 2
        assert len(reloaded.getAnnotations()) == 1
        assert reloaded.getIsAutoValue() is not None
        assert reloaded.getIsAutoValue().getValue() is True
        assert reloaded.getValue() is not None
        assert reloaded.getValue().getValue() == 10.0

    def test_minimal_content_round_trip(self, writer, parser):
        """A parameter value without annotations/isAutoValue/index emits none of those elements."""
        param_value = EcucTextualParamValue()

        parent = ET.Element("PARENT")
        writer.writeEcucTextualParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<INDEX>" not in inner
        assert "<ANNOTATION" not in inner
        assert "<IS-AUTO-VALUE>" not in inner
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucTextualParamValue()
        parser.readEcucTextualParamValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None

    def test_abstract_helper_direct_round_trip(self, writer, parser):
        """The abstract helpers read/write the shared content on a bare parent element (Rule 0001.7)."""
        param_value = EcucTextualParamValue()
        param_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/RteParam").setDest("ECUC-TEXTUAL-PARAM-VALUE"))

        parent = ET.Element("PARENT")
        writer.writeEcucParameterValue(parent, param_value)
        assert parent.find("DEFINITION-REF") is not None

        namespaced = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))[0]
        reloaded = EcucTextualParamValue()
        parser.readEcucParameterValue(namespaced, reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Rte/RteParam"


if __name__ == "__main__":
    pytest.main([__file__])
