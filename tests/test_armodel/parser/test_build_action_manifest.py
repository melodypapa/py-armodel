"""
Reader tests for BuildActionInvocator (AUTOSAR_FO_TPS_GenericStructureTemplate Table 10.6)
and the BuildActionEntity own attributes + Identifiable leveling (Table 10.5).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionEntity, BuildActionInvocator, BuildActionIoElement, BuildEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import UriString
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteBuildActionEntity(BuildActionEntity):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(tag: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<{tag} xmlns='{NS}'>{inner}</{tag}>")


class TestReadBuildActionInvocator:
    def test_read_command_and_sdgs(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("INVOCATION", "<COMMAND>make all</COMMAND>" "<SDGS><SDG><SD GID='ROLE'>PROCESSOR</SD></SDG></SDGS>")
        invocator = parser.readBuildActionInvocator(element, BuildActionInvocator())

        assert str(invocator.getCommand()) == "make all"
        sdgs = invocator.getSdgs()
        assert len(sdgs) == 1

    def test_read_empty_invocation(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("INVOCATION", "")
        invocator = parser.readBuildActionInvocator(element, BuildActionInvocator())

        assert invocator.getCommand() is None
        assert invocator.getSdgs() == []


class TestReadBuildActionEntityInvocation:
    def test_read_invocation_dispatch(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "BUILD-ACTION-ENTITY",
            "<SHORT-NAME>Entity</SHORT-NAME><INVOCATION><COMMAND>make all</COMMAND></INVOCATION>",
        )
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(element, entity)

        invocation = entity.getInvocation()
        assert isinstance(invocation, BuildActionInvocator)
        assert str(invocation.getCommand()) == "make all"

    def test_read_no_invocation(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("BUILD-ACTION-ENTITY", "<SHORT-NAME>Entity</SHORT-NAME>")
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(element, entity)

        assert entity.getInvocation() is None


class TestReadBuildActionEntityDeliveryArtifacts:
    def test_read_delivery_artifacts(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "BUILD-ACTION-ENTITY",
            "<SHORT-NAME>Entity</SHORT-NAME>"
            "<DELIVERY-ARTIFACTS>"
            "<AUTOSAR-ENGINEERING-OBJECT>"
            "<SHORT-LABEL>generated</SHORT-LABEL>"
            "<CATEGORY>SWSRC</CATEGORY>"
            "<REVISION-LABELS><REVISION-LABEL>1.0.0</REVISION-LABEL></REVISION-LABELS>"
            "<DOMAIN>SW</DOMAIN>"
            "</AUTOSAR-ENGINEERING-OBJECT>"
            "<AUTOSAR-ENGINEERING-OBJECT><SHORT-LABEL>documentation</SHORT-LABEL></AUTOSAR-ENGINEERING-OBJECT>"
            "</DELIVERY-ARTIFACTS>",
        )
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(element, entity)

        artifacts = entity.getDeliveryArtifacts()
        assert len(artifacts) == 2
        assert isinstance(artifacts[0], AutosarEngineeringObject)
        assert str(artifacts[0].getShortLabel()) == "generated"
        assert str(artifacts[0].getCategory()) == "SWSRC"
        assert [str(label) for label in artifacts[0].getRevisionLabels()] == ["1.0.0"]
        assert str(artifacts[0].getDomain()) == "SW"
        assert str(artifacts[1].getShortLabel()) == "documentation"

    def test_read_empty_delivery_artifacts_wrapper(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("BUILD-ACTION-ENTITY", "<SHORT-NAME>Entity</SHORT-NAME><DELIVERY-ARTIFACTS/>")
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(element, entity)

        assert entity.getDeliveryArtifacts() == []

    def test_read_absent_delivery_artifacts(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("BUILD-ACTION-ENTITY", "<SHORT-NAME>Entity</SHORT-NAME>")
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(element, entity)

        assert entity.getDeliveryArtifacts() == []


class TestReadBuildActionEntityIdentifiableMembers:
    def test_read_identifiable_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "BUILD-ACTION-ENTITY",
            "<SHORT-NAME>Entity</SHORT-NAME>" "<DESC><L-2 L='EN'>build action entity</L-2></DESC>" "<CATEGORY>BUILD</CATEGORY>",
        )
        element.attrib["UUID"] = "3f2504e0-4f89-11d3-9a0c-0305e82c3301"
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(element, entity)

        assert str(entity.getCategory()) == "BUILD"
        assert entity.getUuid().getValue() == "3f2504e0-4f89-11d3-9a0c-0305e82c3301"
        assert entity.getDesc() is not None


class TestReadBuildEngineeringObject:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "ENGINEERING-OBJECT",
            "<FILE-TYPE>c</FILE-TYPE>"
            "<FILE-TYPE-PATTERN>.*</FILE-TYPE-PATTERN>"
            "<INTENDED-FILENAME>output.c</INTENDED-FILENAME>"
            "<PARENT-CATEGORY>SOURCE</PARENT-CATEGORY>"
            "<PARENT-SHORT-LABEL>root</PARENT-SHORT-LABEL>"
            "<SHORT-LABEL-PATTERN>output_.*</SHORT-LABEL-PATTERN>",
        )
        obj = parser.readBuildEngineeringObject(element, BuildEngineeringObject())

        assert str(obj.getFileType()) == "c"
        assert str(obj.getFileTypePattern()) == ".*"
        assert isinstance(obj.getIntendedFilename(), UriString)
        assert str(obj.getIntendedFilename()) == "output.c"
        assert str(obj.getParentCategory()) == "SOURCE"
        assert str(obj.getParentShortLabel()) == "root"
        assert str(obj.getShortLabelPattern()) == "output_.*"

    def test_read_empty_object(self):
        parser = ARXMLParser(options={"warning": True})
        obj = parser.readBuildEngineeringObject(_snip("ENGINEERING-OBJECT", ""), BuildEngineeringObject())

        assert obj.getFileType() is None
        assert obj.getIntendedFilename() is None


class TestReadBuildActionIoElement:
    def test_read_active_attributes_and_skip_foreign_reference(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "BUILD-ACTION-IO-ELEMENT",
            "<CATEGORY>ARTIFACT</CATEGORY>"
            "<SDGS><SDG><SD GID='ROLE'>PROCESSOR</SD></SDG></SDGS>"
            "<ECUC-DEFINITION-REF DEST='ECUC-MODULE-DEF'>/Ecuc/Definition</ECUC-DEFINITION-REF>"
            "<ENGINEERING-OBJECT><FILE-TYPE>c</FILE-TYPE></ENGINEERING-OBJECT>"
            "<FOREIGN-MODEL-REFERENCE><VALUE>/foreign</VALUE></FOREIGN-MODEL-REFERENCE>"
            "<ROLE>input</ROLE>",
        )
        obj = parser.readBuildActionIoElement(element, BuildActionIoElement())

        assert str(obj.getCategory()) == "ARTIFACT"
        assert len(obj.getSdgs()) == 1
        assert obj.getEcucDefinition().getValue() == "/Ecuc/Definition"
        assert isinstance(obj.getEngineeringObject(), BuildEngineeringObject)
        assert str(obj.getRole()) == "input"
        assert not hasattr(obj, "foreignModelReference")

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        obj = parser.readBuildActionIoElement(_snip("BUILD-ACTION-IO-ELEMENT", ""), BuildActionIoElement())

        assert obj.getCategory() is None
        assert obj.getSdgs() == []
        assert obj.getEngineeringObject() is None
