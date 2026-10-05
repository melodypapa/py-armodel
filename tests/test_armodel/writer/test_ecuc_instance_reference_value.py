"""Reader/writer round-trip tests for EcucInstanceReferenceValue (Table 2.55, XSD complexType ECUC-INSTANCE-REFERENCE-VALUE).

XML element order per the XSD group sequence: AR-OBJECT → ECUC-INDEXABLE-VALUE (INDEX) →
ECUC-ABSTRACT-REFERENCE-VALUE (DEFINITION-REF, ANNOTATIONS, IS-AUTO-VALUE) →
ECUC-INSTANCE-REFERENCE-VALUE (VALUE-IREF last, type AR:ANY-INSTANCE-REF whose group is
CONTEXT-ELEMENT-REF* then TARGET-REF; the atpDerived base association has no XML element).
Table 2.55 has no variationPoint row, so no VARIATION-POINT element may be emitted (Rule 0015).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucInstanceReferenceValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
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


class TestEcucInstanceReferenceValueReadWrite:
    def test_full_content_round_trip(self, writer, parser):
        """All Table 2.55 fields (own VALUE-IREF plus the inherited abstract content) survive a write/read cycle in XSD order."""
        ref_value = EcucInstanceReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/AUTOSAR/EcucDefs/Rte/DataMappings/DataSRMapping/DataElementPrototypeRef").setDest("ECUC-INSTANCE-REFERENCE-DEF"))
        index = PositiveInteger()
        index.setValue("1")
        ref_value.setIndex(index)
        ref_value.addAnnotation(Annotation())
        ref_value.setIsAutoValue(Boolean().setValue(True))
        instance_ref = AnyInstanceRef()
        instance_ref.addContextElementRef(RefType().setValue("/SoftwareComponents/RootComposition/DoorFr").setDest("SW-COMPONENT-PROTOTYPE"))
        instance_ref.setTargetRef(RefType().setValue("/SoftwareComponents/DoorType/DoorAntenna").setDest("R-PORT-PROTOTYPE"))
        ref_value.setValueIRef(instance_ref)

        parent = ET.Element("PARENT")
        writer.writeEcucInstanceReferenceValue(parent, ref_value)
        element = parent.find("ECUC-INSTANCE-REFERENCE-VALUE")
        assert [child.tag for child in element] == ["DEFINITION-REF", "INDEX", "ANNOTATIONS", "IS-AUTO-VALUE", "VALUE-IREF"]
        value_iref = element.find("VALUE-IREF")
        assert [child.tag for child in value_iref] == ["CONTEXT-ELEMENT-REF", "TARGET-REF"]
        assert "<VARIATION-POINT" not in ET.tostring(parent).decode("utf-8")

        reloaded = EcucInstanceReferenceValue()
        parser.readEcucInstanceReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/AUTOSAR/EcucDefs/Rte/DataMappings/DataSRMapping/DataElementPrototypeRef"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 1
        assert len(reloaded.getAnnotations()) == 1
        assert reloaded.getIsAutoValue() is not None
        assert reloaded.getIsAutoValue().getValue() is True
        assert reloaded.getValueIRef() is not None
        assert reloaded.getValueIRef().getContextElementRefs()[0].getValue() == "/SoftwareComponents/RootComposition/DoorFr"
        assert reloaded.getValueIRef().getContextElementRefs()[0].getDest() == "SW-COMPONENT-PROTOTYPE"
        assert reloaded.getValueIRef().getTargetRef().getValue() == "/SoftwareComponents/DoorType/DoorAntenna"
        assert reloaded.getValueIRef().getTargetRef().getDest() == "R-PORT-PROTOTYPE"

    def test_minimal_content_round_trip(self, writer, parser):
        """An instance reference value with only definitionRef set emits no VALUE-IREF and round-trips its field values."""
        ref_value = EcucInstanceReferenceValue()
        ref_value.setDefinitionRef(RefType().setValue("/EcucDefs/Rte/DataMappings/DataSRMapping/DataElementPrototypeRef").setDest("ECUC-INSTANCE-REFERENCE-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucInstanceReferenceValue(parent, ref_value)
        element = parent.find("ECUC-INSTANCE-REFERENCE-VALUE")
        assert element.find("VALUE-IREF") is None
        assert element.find("INDEX") is None
        assert "<VARIATION-POINT" not in ET.tostring(parent).decode("utf-8")

        reloaded = EcucInstanceReferenceValue()
        parser.readEcucInstanceReferenceValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Rte/DataMappings/DataSRMapping/DataElementPrototypeRef"
        assert reloaded.getValueIRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getAnnotations() == []
        assert reloaded.getIsAutoValue() is None

    def test_not_variation_point_capable(self, parser):
        """An incoming VARIATION-POINT element is ignored (Table 2.55 has no variationPoint row, Rule 0015)."""
        raw = (
            "<AUTOSAR xmlns='%s'><ECUC-INSTANCE-REFERENCE-VALUE><DEFINITION-REF DEST='ECUC-INSTANCE-REFERENCE-DEF'>/Def</DEFINITION-REF>"
            "<VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT></ECUC-INSTANCE-REFERENCE-VALUE></AUTOSAR>" % NS
        )
        namespaced = ET.fromstring(raw)[0]
        reloaded = EcucInstanceReferenceValue()
        parser.readEcucInstanceReferenceValue(namespaced, reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/Def"
        assert not hasattr(reloaded, "variationPoint")


if __name__ == "__main__":
    pytest.main([__file__])
