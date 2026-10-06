"""Writer/reader round-trip tests for the SW component port annotations (ApplicationAttributes)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DataLimitKindEnum,
    ProcessingKindEnum,
    ReceiverAnnotation,
    SenderAnnotation,
)
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


def _configure_base(annotation):
    annotation.setComputed(Boolean().setValue(True))
    annotation.setDataElementRef(_ref("/AUTOSAR/DataElement1", "VARIABLE-DATA-PROTOTYPE"))
    annotation.setLimitKind(DataLimitKindEnum().setValue(DataLimitKindEnum.MAX))
    annotation.setProcessingKind(ProcessingKindEnum().setValue(ProcessingKindEnum.FILTERED))


def _serialize(prototype):
    writer = ARXMLWriter()
    parent = ET.Element("P-PORT-PROTOTYPE")
    writer.setPortPrototype(parent, prototype)
    return ET.tostring(parent).decode("utf-8")


def _parse(xml):
    root = ET.fromstring("<AUTOSAR xmlns='http://autosar.org/schema/r4.0'>%s</AUTOSAR>" % xml)
    prototype = PPortPrototype(None, "Port1")
    ARXMLParser().readPPortPrototype(root[0], prototype)
    return prototype


class TestSenderReceiverAnnotationRoundTrip:
    def test_sender_annotation_round_trip(self):
        prototype = PPortPrototype(None, "Port1")
        annotation = SenderAnnotation()
        _configure_base(annotation)
        prototype.addSenderReceiverAnnotation(annotation)

        xml = _serialize(prototype)
        assert "<SENDER-ANNOTATION>" in xml
        assert "<COMPUTED>true</COMPUTED>" in xml
        assert 'DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE"' in xml
        assert "<LIMIT-KIND>MAX</LIMIT-KIND>" in xml
        assert "<PROCESSING-KIND>FILTERED</PROCESSING-KIND>" in xml
        assert "SENDER-RECEIVER-ANNOTATION>" not in xml.replace("SENDER-RECEIVER-ANNOTATIONS", "")

        parsed = _parse(xml)
        annotations = parsed.getSenderReceiverAnnotations()
        assert len(annotations) == 1
        assert isinstance(annotations[0], SenderAnnotation)
        assert annotations[0].getComputed().getValue() is True
        assert annotations[0].getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert annotations[0].getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert annotations[0].getLimitKind().getValue() == DataLimitKindEnum.MAX
        assert annotations[0].getProcessingKind().getValue() == ProcessingKindEnum.FILTERED

    def test_receiver_annotation_round_trip(self):
        prototype = PPortPrototype(None, "Port1")
        annotation = ReceiverAnnotation()
        _configure_base(annotation)
        annotation.setSignalAge(MultidimensionalTime())
        prototype.addSenderReceiverAnnotation(annotation)

        xml = _serialize(prototype)
        assert "<RECEIVER-ANNOTATION>" in xml
        assert "<COMPUTED>true</COMPUTED>" in xml
        assert "<SIGNAL-AGE" in xml

        parsed = _parse(xml)
        annotations = parsed.getSenderReceiverAnnotations()
        assert len(annotations) == 1
        assert isinstance(annotations[0], ReceiverAnnotation)
        assert annotations[0].getComputed().getValue() is True
        assert annotations[0].getDataElementRef().getValue() == "/AUTOSAR/DataElement1"
        assert annotations[0].getSignalAge() is not None

    def test_client_server_annotation_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ClientServerAnnotation

        prototype = PPortPrototype(None, "Port1")
        annotation = ClientServerAnnotation()
        annotation.setOperationRef(_ref("/If/Op", "CLIENT-SERVER-OPERATION"))
        prototype.addClientServerAnnotation(annotation)

        xml = _serialize(prototype)
        assert "<CLIENT-SERVER-ANNOTATION>" in xml
        assert 'OPERATION-REF DEST="CLIENT-SERVER-OPERATION"' in xml

        parsed = _parse(xml)
        annotations = parsed.getClientServerAnnotations()
        assert len(annotations) == 1
        assert isinstance(annotations[0], ClientServerAnnotation)
        assert annotations[0].getOperationRef().getValue() == "/If/Op"
        assert annotations[0].getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

    def test_io_hw_abstraction_server_annotation_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import FilterDebouncingEnum, IoHwAbstractionServerAnnotation

        prototype = PPortPrototype(None, "Port1")
        annotation = IoHwAbstractionServerAnnotation()
        annotation.setAge(MultidimensionalTime())
        annotation.setArgumentRef(_ref("/AUTOSAR/Arg", "ARGUMENT-DATA-PROTOTYPE"))
        annotation.setBswResolution(Float().setValue("1.5"))
        annotation.setDataElementRef(_ref("/AUTOSAR/DataElement1", "VARIABLE-DATA-PROTOTYPE"))
        annotation.setFailureMonitoringRef(_ref("/AUTOSAR/Port2", "PORT-PROTOTYPE"))
        annotation.setFilteringDebouncing(FilterDebouncingEnum().setValue(FilterDebouncingEnum.DEBOUNCE_DATA))
        prototype.addIoHwAbstractionServerAnnotation(annotation)

        xml = _serialize(prototype)
        assert "<IO-HW-ABSTRACTION-SERVER-ANNOTATION>" in xml
        assert "<AGE" in xml
        assert 'ARGUMENT-REF DEST="ARGUMENT-DATA-PROTOTYPE"' in xml
        assert "<BSW-RESOLUTION>1.5</BSW-RESOLUTION>" in xml
        assert "<FILTERING-DEBOUNCING>DEBOUNCE-DATA</FILTERING-DEBOUNCING>" in xml

        parsed = _parse(xml)
        annotations = parsed.getIoHwAbstractionServerAnnotations()
        assert len(annotations) == 1
        assert isinstance(annotations[0], IoHwAbstractionServerAnnotation)
        assert annotations[0].getAge() is not None
        assert annotations[0].getArgumentRef().getValue() == "/AUTOSAR/Arg"
        assert annotations[0].getBswResolution().getValue() == 1.5
        assert annotations[0].getFailureMonitoringRef().getValue() == "/AUTOSAR/Port2"
        assert annotations[0].getFilteringDebouncing().getValue() == FilterDebouncingEnum.DEBOUNCE_DATA

    def test_empty_wrapper_absent(self):
        prototype = PPortPrototype(None, "Port1")
        xml = _serialize(prototype)
        assert "SENDER-RECEIVER-ANNOTATIONS" not in xml
        assert _parse(xml).getSenderReceiverAnnotations() == []
