"""Reader/writer round-trip tests for EcucAddInfoParamValue (Table 2.52, XSD group ECUC-ADD-INFO-PARAM-VALUE).

The single own attribute `value` is a 0..1 DocumentationBlock serialized as the VALUE
element (type AR:DOCUMENTATION-BLOCK). Table 2.52 has no variationPoint row, so no
VARIATION-POINT element may be emitted.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucAddInfoParamValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _make_index(value):
    index = PositiveInteger()
    index.setValue(str(value))
    return index


def _make_doc_block(text):
    doc_block = DocumentationBlock()
    para = MultiLanguageParagraph()
    l1 = LLongName()
    l1.l = "EN"
    l1.value = text
    para.addL1(l1)
    doc_block.addP(para)
    return doc_block


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


class TestEcucAddInfoParamValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """DEFINITION-REF, INDEX and the DocumentationBlock VALUE survive a write/read cycle."""
        param_value = EcucAddInfoParamValue()
        param_value.setDefinitionRef(RefType().setValue("/EcucDefs/Dcm/DcmConfigSet/Dtc").setDest("ECUC-ADD-INFO-PARAM-DEF"))
        param_value.setIndex(_make_index(4))
        param_value.setValue(_make_doc_block("Description of the Dtc 0815."))

        parent = ET.Element("PARENT")
        writer.writeEcucAddInfoParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-ADD-INFO-PARAM-VALUE" in inner
        assert "<VALUE" in inner
        assert "Description of the Dtc 0815." in inner
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucAddInfoParamValue()
        parser.readEcucAddInfoParamValue(_ns_wrap(parent), reloaded)
        assert isinstance(reloaded, EcucAddInfoParamValue)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Dcm/DcmConfigSet/Dtc"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 4
        assert reloaded.getIsAutoValue() is None
        assert isinstance(reloaded.getValue(), DocumentationBlock)
        paras = reloaded.getValue().getPs()
        assert len(paras) == 1
        assert paras[0].getL1s()[0].value == "Description of the Dtc 0815."

    def test_minimal_content_round_trip(self, writer, parser):
        """An add-info parameter value without any content emits no VALUE element and reloads empty."""
        param_value = EcucAddInfoParamValue()

        parent = ET.Element("PARENT")
        writer.writeEcucAddInfoParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-ADD-INFO-PARAM-VALUE" in inner
        assert "<VALUE" not in inner
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucAddInfoParamValue()
        parser.readEcucAddInfoParamValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None
        assert reloaded.getValue() is None


if __name__ == "__main__":
    pytest.main([__file__])
