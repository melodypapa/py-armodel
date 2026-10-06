"""Writer/reader round-trip tests for EndToEndTransformationComSpecProps (Table 4.92, p.201).

The expected XML uses the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group END-TO-END-TRANSFORMATION-COM-SPEC-PROPS),
including the ``E-2-E-PROFILE-COMPATIBILITY-PROPS-REF`` reference element.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, ServerComSpec
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationComSpecProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _full_props():
    props = EndToEndTransformationComSpecProps()
    props.setClearFromValidToInvalid(Boolean().setValue(True))
    props.setDisableEndToEndCheck(Boolean().setValue(True))
    props.setDisableEndToEndStateMachine(Boolean().setValue(True))
    props.setE2eProfileCompatibilityPropsRef(RefType().setValue("/Pkg/Props").setDest("E-2-E-PROFILE-COMPATIBILITY-PROPS"))
    props.setMaxDeltaCounter(PositiveInteger().setValue("3"))
    props.setMaxErrorStateInit(PositiveInteger().setValue("2"))
    props.setMaxErrorStateInvalid(PositiveInteger().setValue("2"))
    props.setMaxErrorStateValid(PositiveInteger().setValue("2"))
    props.setMaxNoNewOrRepeatedData(PositiveInteger().setValue("2"))
    props.setMinOkStateInit(PositiveInteger().setValue("1"))
    props.setMinOkStateInvalid(PositiveInteger().setValue("1"))
    props.setMinOkStateValid(PositiveInteger().setValue("1"))
    props.setSyncCounterInit(PositiveInteger().setValue("0"))
    props.setWindowSizeInit(PositiveInteger().setValue("5"))
    props.setWindowSizeInvalid(PositiveInteger().setValue("5"))
    props.setWindowSizeValid(PositiveInteger().setValue("5"))
    return props


def _assert_full_element(child: ET.Element):
    assert child.tag == "END-TO-END-TRANSFORMATION-COM-SPEC-PROPS"
    assert child.find("CLEAR-FROM-VALID-TO-INVALID").text == "true"
    assert child.find("DISABLE-END-TO-END-CHECK").text == "true"
    assert child.find("DISABLE-END-TO-END-STATE-MACHINE").text == "true"
    ref = child.find("E-2-E-PROFILE-COMPATIBILITY-PROPS-REF")
    assert ref is not None
    assert ref.text == "/Pkg/Props"
    assert ref.attrib["DEST"] == "E-2-E-PROFILE-COMPATIBILITY-PROPS"
    assert child.find("MAX-DELTA-COUNTER").text == "3"
    assert child.find("MAX-ERROR-STATE-INIT").text == "2"
    assert child.find("MAX-ERROR-STATE-INVALID").text == "2"
    assert child.find("MAX-ERROR-STATE-VALID").text == "2"
    assert child.find("MAX-NO-NEW-OR-REPEATED-DATA").text == "2"
    assert child.find("MIN-OK-STATE-INIT").text == "1"
    assert child.find("MIN-OK-STATE-INVALID").text == "1"
    assert child.find("MIN-OK-STATE-VALID").text == "1"
    assert child.find("SYNC-COUNTER-INIT").text == "0"
    assert child.find("WINDOW-SIZE-INIT").text == "5"
    assert child.find("WINDOW-SIZE-INVALID").text == "5"
    assert child.find("WINDOW-SIZE-VALID").text == "5"


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


class TestEndToEndTransformationComSpecPropsWriter:
    def test_write_e2e_transformation_com_spec_props_full(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEndToEndTransformationComSpecProps(parent, _full_props())

        assert len(parent) == 1
        _assert_full_element(parent[0])

    def test_write_e2e_transformation_com_spec_props_empty(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEndToEndTransformationComSpecProps(parent, EndToEndTransformationComSpecProps())

        assert len(parent) == 1
        assert len(parent[0]) == 0

    def test_write_e2e_transformation_com_spec_props_none(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEndToEndTransformationComSpecProps(parent, None)

        assert len(parent) == 0

    def test_write_nonqueued_receiver_com_spec_e2e_props(self, writer):
        com_spec = NonqueuedReceiverComSpec()
        com_spec.addTransformationComSpecProps(_full_props())

        parent = ET.Element("PARENT")
        writer.writeNonqueuedReceiverComSpec(parent, com_spec)

        child = parent.find("NONQUEUED-RECEIVER-COM-SPEC/TRANSFORMATION-COM-SPEC-PROPSS/END-TO-END-TRANSFORMATION-COM-SPEC-PROPS")
        assert child is not None
        assert child.find("MAX-DELTA-COUNTER").text == "3"
        assert child.find("WINDOW-SIZE-INIT").text == "5"

    def test_write_nonqueued_receiver_com_spec_empty_props_no_wrapper(self, writer):
        com_spec = NonqueuedReceiverComSpec()

        parent = ET.Element("PARENT")
        writer.writeNonqueuedReceiverComSpec(parent, com_spec)

        assert parent.find("NONQUEUED-RECEIVER-COM-SPEC/TRANSFORMATION-COM-SPEC-PROPSS") is None


class TestEndToEndTransformationComSpecPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        com_spec = ServerComSpec()
        com_spec.addTransformationComSpecProps(_full_props())

        parent = ET.Element("PARENT")
        writer.writeTransformationComSpecPropss(parent, com_spec.getTransformationComSpecProps())

        out_file = str(tmp_path / "e2e_transformation_com_spec_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        recovered_com_spec = ServerComSpec()
        tree = ET.parse(out_file)
        parser.readTransformationComSpecPropss(tree.getroot()[0], recovered_com_spec)

        props = recovered_com_spec.getTransformationComSpecProps()
        assert len(props) == 1
        recovered = props[0]
        assert isinstance(recovered, EndToEndTransformationComSpecProps)
        assert recovered.getClearFromValidToInvalid().getValue() is True
        assert recovered.getDisableEndToEndCheck().getValue() is True
        assert recovered.getDisableEndToEndStateMachine().getValue() is True
        ref = recovered.getE2eProfileCompatibilityPropsRef()
        assert ref is not None
        assert ref.getValue() == "/Pkg/Props"
        assert ref.getDest() == "E-2-E-PROFILE-COMPATIBILITY-PROPS"
        assert recovered.getMaxDeltaCounter().getValue() == 3
        assert recovered.getMaxErrorStateInit().getValue() == 2
        assert recovered.getMaxErrorStateInvalid().getValue() == 2
        assert recovered.getMaxErrorStateValid().getValue() == 2
        assert recovered.getMaxNoNewOrRepeatedData().getValue() == 2
        assert recovered.getMinOkStateInit().getValue() == 1
        assert recovered.getMinOkStateInvalid().getValue() == 1
        assert recovered.getMinOkStateValid().getValue() == 1
        assert recovered.getSyncCounterInit().getValue() == 0
        assert recovered.getWindowSizeInit().getValue() == 5
        assert recovered.getWindowSizeInvalid().getValue() == 5
        assert recovered.getWindowSizeValid().getValue() == 5
