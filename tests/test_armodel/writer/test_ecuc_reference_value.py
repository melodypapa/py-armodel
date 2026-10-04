"""Reader/writer round-trip tests for EcucReferenceValue (Table 2.54, XSD complexType ECUC-REFERENCE-VALUE).

XML element order per the XSD group sequence: AR-OBJECT → ECUC-INDEXABLE-VALUE (INDEX) →
ECUC-ABSTRACT-REFERENCE-VALUE (DEFINITION-REF, ANNOTATIONS, IS-AUTO-VALUE) →
ECUC-REFERENCE-VALUE (VALUE-REF last). Table 2.54 has no variationPoint row, so no
VARIATION-POINT element may be emitted (Rule 0015).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucReferenceValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
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


def _ns_wrap(parent):
    """Serialize the PARENT's ECUC child under the AUTOSAR namespace and return the ECUC element."""
    return ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))[0][0]


class TestEcucReferenceValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """All Table 2.54 fields (own VALUE-REF plus the inherited abstract content) survive a write/read cycle in XSD order."""
        ref_value = EcucReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/EcucDefs/Os/OsApplication/OsAppScheduleTableRef").setDest("ECUC-REFERENCE-DEF"))
        index = PositiveInteger()
        index.setValue("2")
        ref_value.setIndex(index)
        ref_value.addAnnotation(Annotation())
        ref_value.setIsAutoValue(Boolean().setValue(True))
        ref_value.setValueRef(RefType().setValue("/ECUC/myOs/myOsScheduleTable1").setDest("ECUC-CONTAINER-VALUE"))

        parent = ET.Element("PARENT")
        writer.writeEcucReferenceValue(parent, ref_value)
        element = parent.find("ECUC-REFERENCE-VALUE")
        assert [child.tag for child in element] == ["DEFINITION-REF", "INDEX", "ANNOTATIONS", "IS-AUTO-VALUE", "VALUE-REF"]
        value_ref = element.find("VALUE-REF")
        assert value_ref.text == "/ECUC/myOs/myOsScheduleTable1"
        assert value_ref.attrib["DEST"] == "ECUC-CONTAINER-VALUE"
        assert "<VARIATION-POINT" not in ET.tostring(parent).decode("utf-8")

        reloaded = EcucReferenceValue()
        parser.readEcucReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Os/OsApplication/OsAppScheduleTableRef"
        assert reloaded.getDefinitionRef().getDest() == "ECUC-REFERENCE-DEF"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 2
        assert len(reloaded.getAnnotations()) == 1
        assert reloaded.getIsAutoValue() is not None
        assert reloaded.getIsAutoValue().getValue() is True
        assert reloaded.getValueRef() is not None
        assert reloaded.getValueRef().getValue() == "/ECUC/myOs/myOsScheduleTable1"
        assert reloaded.getValueRef().getDest() == "ECUC-CONTAINER-VALUE"

    def test_minimal_content_round_trip(self, writer, parser):
        """A reference value with only definitionRef set emits no VALUE-REF and round-trips its field values."""
        ref_value = EcucReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/RteRef").setDest("ECUC-REFERENCE-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucReferenceValue(parent, ref_value)
        element = parent.find("ECUC-REFERENCE-VALUE")
        assert element.find("VALUE-REF") is None
        assert element.find("INDEX") is None
        assert "<VARIATION-POINT" not in ET.tostring(parent).decode("utf-8")

        reloaded = EcucReferenceValue()
        parser.readEcucReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Rte/RteRef"
        assert reloaded.getValueRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None

    def test_value_ref_only_round_trip(self, writer, parser):
        """VALUE-REF alone (Example 2.41 shape) survives a write/read cycle."""
        ref_value = EcucReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/AUTOSAR/EcucDefs/Os/OsApplication/OsAppScheduleTableRef").setDest("ECUC-REFERENCE-DEF"))
        ref_value.setValueRef(RefType().setValue("/ECUC/myOs/myOsScheduleTable1").setDest("ECUC-CONTAINER-VALUE"))

        parent = ET.Element("PARENT")
        writer.writeEcucReferenceValue(parent, ref_value)

        reloaded = EcucReferenceValue()
        parser.readEcucReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getValueRef() is not None
        assert reloaded.getValueRef().getValue() == "/ECUC/myOs/myOsScheduleTable1"
        assert reloaded.getValueRef().getDest() == "ECUC-CONTAINER-VALUE"


if __name__ == "__main__":
    pytest.main([__file__])
