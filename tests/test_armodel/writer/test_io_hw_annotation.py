"""Writer/reader round-trip tests for IoHwAbstractionServerAnnotation (PortPrototype annotations)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PPortPrototype
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestIoHwAbstractionServerAnnotationRoundTrip:
    def test_annotation_full_round_trip(self):
        writer = ARXMLWriter()
        parser = ARXMLParser()
        prototype = PPortPrototype(None, "Port1")

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import IoHwAbstractionServerAnnotation

        annotation = IoHwAbstractionServerAnnotation()
        age = MultidimensionalTime()
        annotation.setAge(age)
        annotation.setArgumentRef(_ref("/AUTOSAR/Argument1", "ARGUMENT-DATA-PROTOTYPE"))
        bsw_resolution = Float()
        bsw_resolution.setValue("1.5")
        annotation.setBswResolution(bsw_resolution)
        annotation.setDataElementRef(_ref("/AUTOSAR/DataElement1", "VARIABLE-DATA-PROTOTYPE"))
        annotation.setFailureMonitoringRef(_ref("/AUTOSAR/Port2", "PORT-PROTOTYPE"))
        prototype.addIoHwAbstractionServerAnnotation(annotation)

        parent = ET.Element("P-PORT-PROTOTYPE")
        writer.setPortPrototype(parent, prototype)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<AGE" in inner
        assert 'ARGUMENT-REF DEST="ARGUMENT-DATA-PROTOTYPE"' in inner
        assert "<BSW-RESOLUTION>1.5</BSW-RESOLUTION>" in inner
        assert 'DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE"' in inner
        assert 'FAILURE-MONITORING-REF DEST="PORT-PROTOTYPE"' in inner

        root = ET.fromstring("<AUTOSAR xmlns='http://autosar.org/schema/r4.0'>%s</AUTOSAR>" % inner)
        parsed = PPortPrototype(None, "Port1")
        parser.readPPortPrototype(root[0], parsed)
        annotations = parsed.getIoHwAbstractionServerAnnotations()
        assert len(annotations) == 1
        parsed_annotation = annotations[0]
        assert parsed_annotation.getAge() is not None
        assert parsed_annotation.getArgumentRef().getValue() == "/AUTOSAR/Argument1"
        assert parsed_annotation.getBswResolution().getValue() == 1.5
        assert parsed_annotation.getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert parsed_annotation.getFailureMonitoringRef().getValue() == "/AUTOSAR/Port2"
