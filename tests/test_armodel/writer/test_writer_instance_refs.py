"""Tests for writing ImplicitCommunicationBehavior instance-reference elements."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _ref(value="/Pkg/Elem", dest="DATA-PROTOTYPE-GROUP"):
    r = RefType()
    r.setValue(value)
    r.setDest(dest)
    return r


NS = "http://autosar.org/schema/r4.0"


def _parse_element(xml: str, tag: str) -> ET.Element:
    return ET.fromstring(f"<{tag} xmlns='{NS}'>{xml}</{tag}>")


def _serialize_and_wrap(parent: ET.Element) -> ET.Element:
    inner = ET.tostring(parent).decode("utf-8")
    root = _parse_element(inner, "AUTOSAR")
    return root[0][0]


class TestWriteInnerDataPrototypeGroupInCompositionInstanceRef:
    def test_write_none(self, writer):
        parent = _parent()
        writer.writeInnerDataPrototypeGroupInCompositionInstanceRef(parent, "DATA-PROTOTYPE-GROUP-IN-COMPOSITION-INSTANCE-REF", None)
        assert len(parent) == 0

    def test_write_iref_with_context_and_target(self, writer):
        iref = InnerDataPrototypeGroupInCompositionInstanceRef()
        iref.setBaseRef(_ref("/Swc"))
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/Prototype", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetDataPrototypeGroupRef(_ref("/Comp/Prototype/Group", "DATA-PROTOTYPE-GROUP"))

        parent = _parent()
        writer.writeInnerDataPrototypeGroupInCompositionInstanceRef(parent, "INNER-DATA-PROTOTYPE-GROUP-IN-COMPOSITION-INSTANCE-REF", iref)
        child = parent[0]
        assert child.tag == "INNER-DATA-PROTOTYPE-GROUP-IN-COMPOSITION-INSTANCE-REF"
        assert child.find("CONTEXT-SW-COMPONENT-PROTOTYPE-REF") is not None
        assert child.find("CONTEXT-SW-COMPONENT-PROTOTYPE-REF").text == "/Comp/Prototype"
        assert child.find("TARGET-DATA-PROTOTYPE-GROUP-REF") is not None
        assert child.find("TARGET-DATA-PROTOTYPE-GROUP-REF").text == "/Comp/Prototype/Group"

    def test_round_trip(self, writer, parser):
        iref = InnerDataPrototypeGroupInCompositionInstanceRef()
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/B", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetDataPrototypeGroupRef(_ref("/Comp/A/Group", "DATA-PROTOTYPE-GROUP"))

        parent = _parent()
        writer.writeInnerDataPrototypeGroupInCompositionInstanceRef(parent, "INNER-DATA-PROTOTYPE-GROUP-IN-COMPOSITION-INSTANCE-REF", iref)
        element = _serialize_and_wrap(parent)
        recovered = InnerDataPrototypeGroupInCompositionInstanceRef()
        parser.readInnerDataPrototypeGroupInCompositionInstanceRef(element, recovered)
        assert [r.getValue() for r in recovered.getContextSwComponentPrototypeRefs()] == ["/Comp/A", "/Comp/B"]
        assert recovered.getTargetDataPrototypeGroupRef().getValue() == "/Comp/A/Group"


class TestWriteInnerRunnableEntityGroupInCompositionInstanceRef:
    def test_write_none(self, writer):
        parent = _parent()
        writer.writeInnerRunnableEntityGroupInCompositionInstanceRef(parent, "INNER-RUNNABLE-ENTITY-GROUP-IN-COMPOSITION-INSTANCE-REF", None)
        assert len(parent) == 0

    def test_round_trip(self, writer, parser):
        iref = InnerRunnableEntityGroupInCompositionInstanceRef()
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/B", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetRunnableEntityGroupRef(_ref("/Comp/A/Group", "RUNNABLE-ENTITY-GROUP"))

        parent = _parent()
        writer.writeInnerRunnableEntityGroupInCompositionInstanceRef(parent, "INNER-RUNNABLE-ENTITY-GROUP-IN-COMPOSITION-INSTANCE-REF", iref)
        child = parent[0]
        assert child.tag == "INNER-RUNNABLE-ENTITY-GROUP-IN-COMPOSITION-INSTANCE-REF"
        assert child.find("CONTEXT-SW-COMPONENT-PROTOTYPE-REF") is not None
        assert child.find("TARGET-RUNNABLE-ENTITY-GROUP-REF") is not None

        element = _serialize_and_wrap(parent)
        recovered = InnerRunnableEntityGroupInCompositionInstanceRef()
        parser.readInnerRunnableEntityGroupInCompositionInstanceRef(element, recovered)
        assert [r.getValue() for r in recovered.getContextSwComponentPrototypeRefs()] == ["/Comp/A", "/Comp/B"]
        assert recovered.getTargetRunnableEntityGroupRef().getValue() == "/Comp/A/Group"


class TestWriteRunnableEntityInCompositionInstanceRef:
    def test_write_none(self, writer):
        parent = _parent()
        writer.writeRunnableEntityInCompositionInstanceRef(parent, "RUNNABLE-ENTITY-IN-COMPOSITION-INSTANCE-REF", None)
        assert len(parent) == 0

    def test_round_trip(self, writer, parser):
        iref = RunnableEntityInCompositionInstanceRef()
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetRunnableEntityRef(_ref("/Comp/A/Behavior/Entity", "RUNNABLE-ENTITY"))

        parent = _parent()
        writer.writeRunnableEntityInCompositionInstanceRef(parent, "RUNNABLE-ENTITY-IN-COMPOSITION-INSTANCE-REF", iref)
        child = parent[0]
        assert child.tag == "RUNNABLE-ENTITY-IN-COMPOSITION-INSTANCE-REF"
        assert child.find("CONTEXT-SW-COMPONENT-PROTOTYPE-REF") is not None
        assert child.find("TARGET-RUNNABLE-ENTITY-REF") is not None

        element = _serialize_and_wrap(parent)
        recovered = RunnableEntityInCompositionInstanceRef()
        parser.readRunnableEntityInCompositionInstanceRef(element, recovered)
        assert [r.getValue() for r in recovered.getContextSwComponentPrototypeRefs()] == ["/Comp/A"]
        assert recovered.getTargetRunnableEntityRef().getValue() == "/Comp/A/Behavior/Entity"


class TestWriteVariableDataPrototypeInCompositionInstanceRef:
    def test_write_none(self, writer):
        parent = _parent()
        writer.writeVariableDataPrototypeInCompositionInstanceRef(parent, "VARIABLE-DATA-PROTOTYPE-IN-COMPOSITION-INSTANCE-REF", None)
        assert len(parent) == 0

    def test_round_trip(self, writer, parser):
        iref = VariableDataPrototypeInCompositionInstanceRef()
        iref.setContextPortPrototypeRef(_ref("/Comp/A/PPort", "P-PORT-PROTOTYPE"))
        iref.addContextSwComponentPrototypeRef(_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetVariableDataPrototypeRef(_ref("/Comp/A/PPort/Data", "VARIABLE-DATA-PROTOTYPE"))

        parent = _parent()
        writer.writeVariableDataPrototypeInCompositionInstanceRef(parent, "VARIABLE-DATA-PROTOTYPE-IN-COMPOSITION-INSTANCE-REF", iref)
        child = parent[0]
        assert child.tag == "VARIABLE-DATA-PROTOTYPE-IN-COMPOSITION-INSTANCE-REF"
        assert child.find("CONTEXT-PORT-PROTOTYPE-REF") is not None
        assert child.find("CONTEXT-SW-COMPONENT-PROTOTYPE-REF") is not None
        assert child.find("TARGET-VARIABLE-DATA-PROTOTYPE-REF") is not None

        element = _serialize_and_wrap(parent)
        recovered = VariableDataPrototypeInCompositionInstanceRef()
        parser.readVariableDataPrototypeInCompositionInstanceRef(element, recovered)
        assert recovered.getContextPortPrototypeRef().getValue() == "/Comp/A/PPort"
        assert [r.getValue() for r in recovered.getContextSwComponentPrototypeRefs()] == ["/Comp/A"]
        assert recovered.getTargetVariableDataPrototypeRef().getValue() == "/Comp/A/PPort/Data"

    def test_round_trip_empty_wrapper(self, writer, parser):
        iref = VariableDataPrototypeInCompositionInstanceRef()
        parent = _parent()
        writer.writeVariableDataPrototypeInCompositionInstanceRef(parent, "VARIABLE-DATA-PROTOTYPE-IN-COMPOSITION-INSTANCE-REF", iref)
        element = _serialize_and_wrap(parent)
        recovered = VariableDataPrototypeInCompositionInstanceRef()
        parser.readVariableDataPrototypeInCompositionInstanceRef(element, recovered)
        assert recovered.getContextPortPrototypeRef() is None
        assert recovered.getContextSwComponentPrototypeRefs() == []
        assert recovered.getTargetVariableDataPrototypeRef() is None
