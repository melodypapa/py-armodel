"""Reader/writer round-trip tests for EcucAbstractReferenceValue (abstract, XSD group ECUC-ABSTRACT-REFERENCE-VALUE).

EcucAbstractReferenceValue has no standalone XML element: its content (DEFINITION-REF,
ANNOTATION, IS-AUTO-VALUE) is serialized inside the concrete subclasses (EcucReferenceValue,
EcucInstanceReferenceValue). Coverage therefore exercises the reusable
readEcucAbstractReferenceValue / writeEcucAbstractReferenceValue helpers through the concrete
readers/writers that call them. Table 2.53 has no variationPoint row, so no VARIATION-POINT
element may be emitted (Rule 0015).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucInstanceReferenceValue,
    EcucReferenceValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
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


class TestEcucAbstractReferenceValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """DEFINITION-REF, INDEX, ANNOTATION and IS-AUTO-VALUE survive a write/read cycle in XSD order."""
        ref_value = EcucReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/EcucDefs/Os/OsOS/OsRef").setDest("ECUC-REFERENCE-DEF"))
        ref_value.setIndex(_make_index(3))
        ref_value.addAnnotation(Annotation())
        ref_value.setIsAutoValue(_make_boolean(True))
        ref_value.setValueRef(RefType().setValue("/ECUC/myOs/myOsScheduleTable1").setDest("ECUC-CONTAINER-VALUE"))

        parent = ET.Element("PARENT")
        writer.writeEcucReferenceValue(parent, ref_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-REFERENCE-VALUE>" in inner
        assert inner.index("<DEFINITION-REF") < inner.index("<INDEX>") < inner.index("<ANNOTATION") < inner.index("<IS-AUTO-VALUE>")
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucReferenceValue()
        parser.readEcucReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Os/OsOS/OsRef"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 3
        assert len(reloaded.getAnnotations()) == 1
        assert reloaded.getIsAutoValue() is not None
        assert reloaded.getIsAutoValue().getValue() is True

    def test_minimal_content_round_trip(self, writer, parser):
        """A reference value without annotations/isAutoValue/index emits none of those elements."""
        ref_value = EcucInstanceReferenceValue()

        parent = ET.Element("PARENT")
        writer.writeEcucInstanceReferenceValue(parent, ref_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<INDEX>" not in inner
        assert "<ANNOTATION" not in inner
        assert "<IS-AUTO-VALUE>" not in inner
        assert "<VARIATION-POINT" not in inner

        reloaded = EcucInstanceReferenceValue()
        parser.readEcucInstanceReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None
        assert reloaded.getValueIRef() is None

    def test_abstract_helper_direct_round_trip(self, writer, parser):
        """The abstract helpers read/write the shared content on a bare parent element (Rule 0001.7)."""
        ref_value = EcucReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/RteRef").setDest("ECUC-REFERENCE-DEF"))
        ref_value.addAnnotation(Annotation())

        parent = ET.Element("PARENT")
        writer.writeEcucAbstractReferenceValue(parent, ref_value)
        assert parent.find("DEFINITION-REF") is not None
        assert parent.find("ANNOTATIONS") is not None

        namespaced = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))[0]
        reloaded = EcucReferenceValue()
        parser.readEcucAbstractReferenceValue(namespaced, reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Rte/RteRef"
        assert len(reloaded.getAnnotations()) == 1

    def test_no_variation_point_read_or_written(self, writer, parser):
        """Table 2.53 has no variationPoint row (Rule 0015): an incoming VARIATION-POINT is ignored and none is emitted."""
        ref_value = EcucReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/RteRef").setDest("ECUC-REFERENCE-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucReferenceValue(parent, ref_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<VARIATION-POINT" not in inner

        raw = (
            "<AUTOSAR xmlns='%s'><ECUC-REFERENCE-VALUE><DEFINITION-REF DEST='ECUC-REFERENCE-DEF'>/Def</DEFINITION-REF><VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT></ECUC-REFERENCE-VALUE></AUTOSAR>"
            % NS
        )
        namespaced = ET.fromstring(raw)[0]
        reloaded = EcucReferenceValue()
        parser.readEcucAbstractReferenceValue(namespaced, reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/Def"
        assert not hasattr(reloaded, "variationPoint")

    def test_instance_reference_value_iref_round_trip(self, writer, parser):
        """VALUE-IREF (AnyInstanceRef) survives a write/read cycle inside an EcucInstanceReferenceValue."""
        ref_value = EcucInstanceReferenceValue()
        instance_ref = AnyInstanceRef()
        instance_ref.addContextElementRef(RefType().setValue("/SoftwareComponents/RootComposition/DoorFr").setDest("SW-COMPONENT-PROTOTYPE"))
        instance_ref.addContextElementRef(RefType().setValue("/SoftwareComponents/DoorType").setDest("COMPOSITION-PROTOTYPE"))
        instance_ref.setTargetRef(RefType().setValue("/SoftwareComponents/DoorType/DoorAntenna").setDest("R-PORT-PROTOTYPE"))
        ref_value.setValueIRef(instance_ref)

        parent = ET.Element("PARENT")
        writer.writeEcucInstanceReferenceValue(parent, ref_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<VALUE-IREF>" in inner
        assert "<CONTEXT-ELEMENT-REF" in inner
        assert "<TARGET-REF" in inner

        reloaded = EcucInstanceReferenceValue()
        parser.readEcucInstanceReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getValueIRef() is not None
        assert [ref.getValue() for ref in reloaded.getValueIRef().getContextElementRefs()] == ["/SoftwareComponents/RootComposition/DoorFr", "/SoftwareComponents/DoorType"]
        assert reloaded.getValueIRef().getTargetRef().getValue() == "/SoftwareComponents/DoorType/DoorAntenna"


if __name__ == "__main__":
    pytest.main([__file__])
