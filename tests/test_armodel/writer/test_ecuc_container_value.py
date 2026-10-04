"""Reader/writer round-trip tests for EcucContainerValue (Table 2.48, XSD group ECUC-CONTAINER-VALUE).

XML element order per the XSD group sequence: DEFINITION-REF, PARAMETER-VALUES, REFERENCE-VALUES,
SUB-CONTAINERS (the VARIATION-POINT element is an atpVariation artifact and is not modeled).
Table 2.48 has no variationPoint row (Rule 0015), so no VARIATION-POINT element may be emitted.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAddInfoParamValue,
    EcucContainerValue,
    EcucInstanceReferenceValue,
    EcucNumericalParamValue,
    EcucReferenceValue,
    EcucTextualParamValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical, PositiveInteger, RefType, VerbatimString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _make_index(value):
    index = PositiveInteger()
    index.setValue(str(value))
    return index


def _make_definition_ref(value, dest):
    return RefType().setValue(value).setDest(dest)


def _make_numerical(value):
    return Numerical().setValue(value)


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


class TestEcucContainerValueReadWrite:
    def test_full_nested_content_round_trip(self, writer, parser):
        """DEFINITION-REF, INDEX, PARAMETER-VALUES, REFERENCE-VALUES and SUB-CONTAINERS survive a write/read cycle in XSD order, with the nested content asserted one level down."""
        container = EcucContainerValue(None, "RteGeneration")
        container.setDefinitionRef(_make_definition_ref("/AUTOSAR/EcucDefs/Rte/RteGeneration", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        container.setIndex(_make_index(2))

        numerical = EcucNumericalParamValue()
        numerical.setDefinitionRef(_make_definition_ref("/AUTOSAR/EcucDefs/Rte/RteGeneration/RteBswModuleConfiguration", "ECUC-INTEGER-PARAM-DEF"))
        numerical.setValue(_make_numerical("74.8"))
        container.addParameterValue(numerical)

        textual = EcucTextualParamValue()
        textual.setValue(VerbatimString().setValue("NVM_BLOCK_NATIVE"))
        container.addParameterValue(textual)

        reference = EcucReferenceValue()
        reference.setValueRef(RefType().setValue("/ECUC/myOs/myOsScheduleTable1").setDest("ECUC-CONTAINER-VALUE"))
        container.addReferenceValue(reference)

        sub_container = container.createSubContainer("SwComponentInstance")
        sub_container.setDefinitionRef(_make_definition_ref("/AUTOSAR/EcucDefs/Rte/RteGeneration/SwComponentInstance", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        sub_reference = EcucInstanceReferenceValue()
        instance_ref = AnyInstanceRef()
        instance_ref.addContextElementRef(RefType().setValue("/SoftwareComponents/RootComposition/DoorFr").setDest("SW-COMPONENT-PROTOTYPE"))
        instance_ref.setTargetRef(RefType().setValue("/SoftwareComponents/DoorType/DoorAntenna").setDest("R-PORT-PROTOTYPE"))
        sub_reference.setValueIRef(instance_ref)
        sub_container.addReferenceValue(sub_reference)

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        element = parent.find("ECUC-CONTAINER-VALUE")
        assert [elem.tag for elem in element] == ["SHORT-NAME", "DEFINITION-REF", "INDEX", "PARAMETER-VALUES", "REFERENCE-VALUES", "SUB-CONTAINERS"]

        param_values_element = element.find("PARAMETER-VALUES")
        assert [elem.tag for elem in param_values_element] == ["ECUC-NUMERICAL-PARAM-VALUE", "ECUC-TEXTUAL-PARAM-VALUE"]
        reference_values_element = element.find("REFERENCE-VALUES")
        assert [elem.tag for elem in reference_values_element] == ["ECUC-REFERENCE-VALUE"]
        sub_containers_element = element.find("SUB-CONTAINERS")
        assert [elem.tag for elem in sub_containers_element] == ["ECUC-CONTAINER-VALUE"]

        reloaded = EcucContainerValue(None, "RteGeneration")
        parser.readEcucContainerValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/AUTOSAR/EcucDefs/Rte/RteGeneration"
        assert reloaded.getIndex() is not None
        assert reloaded.getIndex().getValue() == 2

        assert len(reloaded.getParameterValues()) == 2
        reloaded_numerical = reloaded.getParameterValues()[0]
        assert isinstance(reloaded_numerical, EcucNumericalParamValue)
        assert reloaded_numerical.getDefinitionRef().getValue() == "/AUTOSAR/EcucDefs/Rte/RteGeneration/RteBswModuleConfiguration"
        assert reloaded_numerical.getValue() is not None
        assert reloaded_numerical.getValue().getValue() == 74.8
        reloaded_textual = reloaded.getParameterValues()[1]
        assert isinstance(reloaded_textual, EcucTextualParamValue)
        assert reloaded_textual.getValue() is not None
        assert reloaded_textual.getValue().getValue() == "NVM_BLOCK_NATIVE"

        assert len(reloaded.getReferenceValues()) == 1
        reloaded_reference = reloaded.getReferenceValues()[0]
        assert isinstance(reloaded_reference, EcucReferenceValue)
        assert reloaded_reference.getValueRef().getValue() == "/ECUC/myOs/myOsScheduleTable1"

        assert len(reloaded.getSubContainers()) == 1
        reloaded_sub = reloaded.getSubContainers()[0]
        assert reloaded_sub.short_name == "SwComponentInstance"
        assert reloaded_sub.getDefinitionRef().getValue() == "/AUTOSAR/EcucDefs/Rte/RteGeneration/SwComponentInstance"
        assert len(reloaded_sub.getReferenceValues()) == 1
        reloaded_sub_reference = reloaded_sub.getReferenceValues()[0]
        assert isinstance(reloaded_sub_reference, EcucInstanceReferenceValue)
        assert reloaded_sub_reference.getValueIRef() is not None
        assert [ref.getValue() for ref in reloaded_sub_reference.getValueIRef().getContextElementRefs()] == ["/SoftwareComponents/RootComposition/DoorFr"]
        assert reloaded_sub_reference.getValueIRef().getTargetRef().getValue() == "/SoftwareComponents/DoorType/DoorAntenna"

    def test_minimal_content_round_trip(self, writer, parser):
        """A container without definition/index/aggregations emits none of those wrapper elements."""
        container = EcucContainerValue(None, "EmptyContainer")

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        element = parent.find("ECUC-CONTAINER-VALUE")
        assert [elem.tag for elem in element] == ["SHORT-NAME"]
        assert "<VARIATION-POINT" not in ET.tostring(parent).decode("utf-8")

        reloaded = EcucContainerValue(None, "EmptyContainer")
        parser.readEcucContainerValue(_ns_wrap(parent), reloaded)
        assert reloaded.getDefinitionRef() is None
        assert reloaded.getIndex() is None
        assert reloaded.getParameterValues() == []
        assert reloaded.getReferenceValues() == []
        assert reloaded.getSubContainers() == []

    def test_add_info_param_value_round_trip(self, writer, parser):
        """An ECUC-ADD-INFO-PARAM-VALUE aggregation survives the write/read cycle with its DocumentationBlock value."""
        container = EcucContainerValue(None, "WithAddInfo")
        add_info = EcucAddInfoParamValue()
        add_info.setDefinitionRef(_make_definition_ref("/AUTOSAR/EcucDefs/Rte/RteGeneration/AddInfo", "ECUC-ADD-INFO-PARAM-DEF"))
        container.addParameterValue(add_info)

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-ADD-INFO-PARAM-VALUE>" in inner

        reloaded = EcucContainerValue(None, "WithAddInfo")
        parser.readEcucContainerValue(_ns_wrap(parent), reloaded)
        assert len(reloaded.getParameterValues()) == 1
        reloaded_add_info = reloaded.getParameterValues()[0]
        assert isinstance(reloaded_add_info, EcucAddInfoParamValue)
        assert reloaded_add_info.getDefinitionRef().getValue() == "/AUTOSAR/EcucDefs/Rte/RteGeneration/AddInfo"

    def test_no_variation_point_read_or_written(self, writer, parser):
        """Table 2.48 has no variationPoint row (Rule 0015): an incoming VARIATION-POINT is ignored and none is emitted."""
        container = EcucContainerValue(None, "NoVp")
        container.setDefinitionRef(_make_definition_ref("/AUTOSAR/EcucDefs/Rte/RteGeneration", "ECUC-PARAM-CONF-CONTAINER-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<VARIATION-POINT" not in inner

        raw = (
            "<AUTOSAR xmlns='%s'><ECUC-CONTAINER-VALUE><SHORT-NAME>NoVp</SHORT-NAME><DEFINITION-REF DEST='ECUC-PARAM-CONF-CONTAINER-DEF'>/Def</DEFINITION-REF><VARIATION-POINT><SHORT-LABEL>vp1</SHORT-LABEL></VARIATION-POINT></ECUC-CONTAINER-VALUE></AUTOSAR>"
            % NS
        )
        namespaced = ET.fromstring(raw)[0]
        reloaded = EcucContainerValue(None, "NoVp")
        parser.readEcucContainerValue(namespaced, reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/Def"
        assert not hasattr(reloaded, "variationPoint")

    def test_nested_sub_container_duplicate_short_name_round_trip(self, writer, parser):
        """Two sibling sub-containers with distinct short names round-trip in order via the dedicated typed list."""
        container = EcucContainerValue(None, "Parent")
        first = container.createSubContainer("First")
        first.setDefinitionRef(_make_definition_ref("/EcucDefs/First", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        second = container.createSubContainer("Second")
        second.setDefinitionRef(_make_definition_ref("/EcucDefs/Second", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        duplicate = container.createSubContainer("First")
        assert duplicate is first

        parent = ET.Element("PARENT")
        writer.writeEcucContainValue(parent, container)
        sub_containers_element = parent.find("ECUC-CONTAINER-VALUE").find("SUB-CONTAINERS")
        assert [elem.tag for elem in sub_containers_element] == ["ECUC-CONTAINER-VALUE", "ECUC-CONTAINER-VALUE"]

        reloaded = EcucContainerValue(None, "Parent")
        parser.readEcucContainerValue(_ns_wrap(parent), reloaded)
        assert [sub.short_name for sub in reloaded.getSubContainers()] == ["First", "Second"]
        assert reloaded.getSubContainers()[0].getDefinitionRef().getValue() == "/EcucDefs/First"
        assert reloaded.getSubContainers()[1].getDefinitionRef().getValue() == "/EcucDefs/Second"


if __name__ == "__main__":
    pytest.main([__file__])
