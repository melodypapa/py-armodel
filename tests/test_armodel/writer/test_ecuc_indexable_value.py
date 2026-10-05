"""Reader/writer round-trip tests for EcucIndexableValue (abstract, XSD group ECUC-INDEXABLE-VALUE).

EcucIndexableValue has no standalone XML element: its INDEX group is serialized inside the
concrete subclasses (EcucContainerValue, EcucParameterValue family, EcucAbstractReferenceValue
family). Coverage therefore exercises the reusable readEcucIndexableValue / writeEcucIndexableValue
helpers both directly and through the concrete readers/writers that call them.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucContainerValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucReferenceValue,
    EcucTextualParamValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, VerbatimString
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


def _index(value):
    index = PositiveInteger()
    index.setValue(str(value))
    return index


def _make_container(short_name):
    values = EcucModuleConfigurationValues(None, "mcv")
    return values.createContainer(short_name)


def _ns_wrap(parent):
    return ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent[0]).decode("utf-8")))


class TestEcucIndexableValueReadWrite:
    def test_shared_helper_round_trip(self, writer, parser):
        """The abstract base owns reusable read/write helpers for its INDEX group (Rule 0001.7)."""
        value = EcucNumericalParamValue()
        value.setIndex(_index(4))

        parent = ET.Element("PARENT")
        writer.writeEcucIndexableValue(parent, value)
        index_element = parent.find("INDEX")
        assert index_element is not None
        assert index_element.text == "4"

        namespaced_parent = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))[0]
        reloaded = EcucNumericalParamValue()
        parser.readEcucIndexableValue(namespaced_parent, reloaded)
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 4

    def test_container_value_index_round_trip(self, writer, parser):
        """readEcucContainerValue/writeEcucContainValue go through the shared indexable helpers."""
        container = _make_container("cv")
        container.setDefinitionRef(RefType().setValue("/EcucDefs/Os/OsOS").setDest("ECUC-PARAM-CONF-CONTAINER-DEF"))
        container.setIndex(_index(7))

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-CONTAINER-VALUE>" in inner
        assert "<INDEX>7</INDEX>" in inner
        assert inner.index("<DEFINITION-REF") < inner.index("<INDEX>")

        reloaded = EcucContainerValue(None, "cv")
        parser.readEcucContainerValue(_ns_wrap(parent)[0], reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Os/OsOS"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 7

    def test_parameter_value_index_round_trip(self, writer, parser):
        """readEcucParameterValue/writeEcucParameterValue go through the shared indexable helpers."""
        param_value = EcucTextualParamValue()
        param_value.setDefinitionRef(RefType().setValue("/EcucDefs/Os/OsOS/OsParam").setDest("ECUC-TEXTUAL-PARAM-VALUE"))
        param_value.setIndex(_index(2))
        param_value.setValue(VerbatimString().setValue("v"))

        parent = ET.Element("PARENT")
        writer.writeEcucTextualParamValue(parent, param_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<INDEX>2</INDEX>" in inner

        reloaded = EcucTextualParamValue()
        parser.readEcucTextualParamValue(_ns_wrap(parent)[0], reloaded)
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 2
        assert reloaded.getValue() is not None
        assert reloaded.getValue().getValue() == "v"

    def test_reference_value_index_round_trip(self, writer, parser):
        """readEcucAbstractReferenceValue/writeEcucAbstractReferenceValue go through the shared indexable helpers."""
        reference_value = EcucReferenceValue()
        reference_value.setDefinitionRef(RefType().setValue("/EcucDefs/Os/OsOS/OsRef").setDest("ECUC-REFERENCE-VALUE"))
        reference_value.setIndex(_index(3))
        reference_value.setValueRef(RefType().setValue("/Ecuc/Task").setDest("ECUC-PARAM-CONF-CONTAINER-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucReferenceValue(parent, reference_value)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<INDEX>3</INDEX>" in inner

        reloaded = EcucReferenceValue()
        parser.readEcucReferenceValue(_ns_wrap(parent)[0], reloaded)
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 3
        assert reloaded.getValueRef() is not None
        assert reloaded.getValueRef().getValue() == "/Ecuc/Task"

    def test_index_absent_round_trip(self, writer, parser):
        """A None index emits no INDEX element and reloads as None."""
        container = _make_container("cv")

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        container_element = parent.find("ECUC-CONTAINER-VALUE")
        assert container_element is not None
        assert container_element.find("INDEX") is None

        reloaded = EcucContainerValue(None, "cv")
        parser.readEcucContainerValue(_ns_wrap(parent)[0], reloaded)
        assert reloaded.getIndex() is None
