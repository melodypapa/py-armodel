"""
Writer tests for BuildActionInvocator (AUTOSAR_FO_TPS_GenericStructureTemplate Table 10.6)
and the BuildActionEntity own attributes + Identifiable leveling (Table 10.5).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionEntity, BuildActionInvocator, BuildActionIoElement, BuildEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType, RegularExpression, RevisionLabelString, String, UriString, VerbatimString
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteBuildActionEntity(BuildActionEntity):
    pass


def _namespaced_wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element, encoding="unicode")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")[0]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestWriteBuildActionInvocator:
    def test_write_command_and_sdgs(self):
        writer = ARXMLWriter()
        invocator = BuildActionInvocator()
        command = VerbatimString()
        command.setValue("make all")
        invocator.setCommand(command)
        invocator.addSdg(Sdg())

        element = ET.Element("INVOCATION")
        writer.writeBuildActionInvocator(element, invocator)

        assert element.find("COMMAND").text == "make all"
        assert element.find("SDGS/SDG") is not None

    def test_write_empty_invocator_omits_optional_children(self):
        writer = ARXMLWriter()
        invocator = BuildActionInvocator()

        element = ET.Element("INVOCATION")
        writer.writeBuildActionInvocator(element, invocator)

        assert element.find("COMMAND") is None
        assert element.find("SDGS") is None


class TestWriteBuildActionEntityInvocation:
    def test_write_invocation_dispatch(self):
        writer = ARXMLWriter()
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        invocator = BuildActionInvocator()
        command = VerbatimString()
        command.setValue("make all")
        invocator.setCommand(command)
        entity.setInvocation(invocator)

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)

        assert element.find("INVOCATION/COMMAND").text == "make all"

    def test_write_no_invocation_omits_element(self):
        writer = ARXMLWriter()
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)

        assert element.find("INVOCATION") is None


def _artifact(short_label: str, category: str = None, revision_label: str = None, domain: str = None) -> AutosarEngineeringObject:
    artifact = AutosarEngineeringObject()
    label = NameToken()
    label.setValue(short_label)
    artifact.setShortLabel(label)
    if category is not None:
        category_value = NameToken()
        category_value.setValue(category)
        artifact.setCategory(category_value)
    if revision_label is not None:
        revision = RevisionLabelString()
        revision.setValue(revision_label)
        artifact.addRevisionLabel(revision)
    if domain is not None:
        domain_value = NameToken()
        domain_value.setValue(domain)
        artifact.setDomain(domain_value)
    return artifact


class TestWriteBuildActionEntityDeliveryArtifacts:
    def test_write_delivery_artifacts(self):
        writer = ARXMLWriter()
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        entity.addDeliveryArtifact(_artifact("generated", category="SWSRC", revision_label="1.0.0", domain="SW"))
        entity.addDeliveryArtifact(_artifact("documentation"))

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)

        artifacts = element.findall("DELIVERY-ARTIFACTS/AUTOSAR-ENGINEERING-OBJECT")
        assert len(artifacts) == 2
        assert artifacts[0].find("SHORT-LABEL").text == "generated"
        assert artifacts[0].find("CATEGORY").text == "SWSRC"
        assert artifacts[0].find("REVISION-LABELS/REVISION-LABEL").text == "1.0.0"
        assert artifacts[0].find("DOMAIN").text == "SW"
        assert artifacts[1].find("SHORT-LABEL").text == "documentation"

    def test_write_empty_delivery_artifacts_omits_wrapper(self):
        writer = ARXMLWriter()
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)

        assert element.find("DELIVERY-ARTIFACTS") is None


class TestWriteBuildActionEntityIdentifiableMembers:
    def test_write_identifiable_members(self):
        writer = ARXMLWriter()
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        category = NameToken()
        category.setValue("BUILD")
        entity.setCategory(category)
        uuid = String()
        uuid.setValue("3f2504e0-4f89-11d3-9a0c-0305e82c3301")
        entity.setUuid(uuid)

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)

        assert element.find("SHORT-NAME").text == "Entity"
        assert element.find("CATEGORY").text == "BUILD"
        assert element.attrib["UUID"] == "3f2504e0-4f89-11d3-9a0c-0305e82c3301"


class TestBuildActionEntityRoundTrip:
    def test_round_trip_preserves_values(self):
        writer = ARXMLWriter()
        parser = ARXMLParser(options={"warning": True})
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        category = NameToken()
        category.setValue("BUILD")
        entity.setCategory(category)
        entity.addDeliveryArtifact(_artifact("generated", category="SWSRC", revision_label="1.0.0", domain="SW"))
        invocator = BuildActionInvocator()
        command = VerbatimString()
        command.setValue("make all")
        invocator.setCommand(command)
        entity.setInvocation(invocator)

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)

        reloaded_element = _namespaced_wrap(element)
        AUTOSAR.getInstance().new()
        reloaded = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(reloaded_element, reloaded)

        assert str(reloaded.getCategory()) == "BUILD"
        artifacts = reloaded.getDeliveryArtifacts()
        assert len(artifacts) == 1
        assert str(artifacts[0].getShortLabel()) == "generated"
        assert str(artifacts[0].getCategory()) == "SWSRC"
        assert [str(label) for label in artifacts[0].getRevisionLabels()] == ["1.0.0"]
        assert str(artifacts[0].getDomain()) == "SW"
        assert str(reloaded.getInvocation().getCommand()) == "make all"

    def test_round_trip_empty_entity_omits_wrappers(self):
        writer = ARXMLWriter()
        parser = ARXMLParser(options={"warning": True})
        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")

        element = ET.Element("BUILD-ACTION-ENTITY")
        writer.writeBuildActionEntity(element, entity)
        serialized = ET.tostring(element, encoding="unicode")

        assert "DELIVERY-ARTIFACTS" not in serialized
        assert "INVOCATION" not in serialized

        AUTOSAR.getInstance().new()
        reloaded = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        parser.readBuildActionEntity(_namespaced_wrap(ET.fromstring(serialized)), reloaded)

        assert reloaded.getDeliveryArtifacts() == []
        assert reloaded.getInvocation() is None
        assert reloaded.getCategory() is None


class TestWriteBuildEngineeringObject:
    def test_write_all_attributes(self):
        writer = ARXMLWriter()
        obj = BuildEngineeringObject()
        file_type = NameToken()
        file_type.setValue("c")
        file_type_pattern = RegularExpression()
        file_type_pattern.setValue(".*")
        intended_filename = UriString()
        intended_filename.setValue("output.c")
        parent_category = NameToken()
        parent_category.setValue("SOURCE")
        parent_short_label = NameToken()
        parent_short_label.setValue("root")
        short_label_pattern = RegularExpression()
        short_label_pattern.setValue("output_.*")
        obj.setFileType(file_type)
        obj.setFileTypePattern(file_type_pattern)
        obj.setIntendedFilename(intended_filename)
        obj.setParentCategory(parent_category)
        obj.setParentShortLabel(parent_short_label)
        obj.setShortLabelPattern(short_label_pattern)

        element = ET.Element("ENGINEERING-OBJECT")
        writer.writeBuildEngineeringObject(element, obj)

        assert element.find("FILE-TYPE").text == "c"
        assert element.find("FILE-TYPE-PATTERN").text == ".*"
        assert element.find("INTENDED-FILENAME").text == "output.c"
        assert element.find("PARENT-CATEGORY").text == "SOURCE"
        assert element.find("PARENT-SHORT-LABEL").text == "root"
        assert element.find("SHORT-LABEL-PATTERN").text == "output_.*"

    def test_write_empty_object(self):
        writer = ARXMLWriter()
        element = ET.Element("ENGINEERING-OBJECT")
        writer.writeBuildEngineeringObject(element, BuildEngineeringObject())

        assert list(element) == []


class TestWriteBuildActionIoElement:
    def test_write_active_attributes_without_skipped_foreign_reference(self):
        writer = ARXMLWriter()
        obj = BuildActionIoElement()
        category = VerbatimString()
        category.setValue("ARTIFACT")
        role = VerbatimString()
        role.setValue("input")
        ref = RefType()
        ref.setValue("/Ecuc/Definition")
        engineering_object = BuildEngineeringObject()
        file_type = NameToken()
        file_type.setValue("c")
        engineering_object.setFileType(file_type)
        obj.setCategory(category).setRole(role).setEcucDefinition(ref).setEngineeringObject(engineering_object)
        obj.addSdg(Sdg())

        element = ET.Element("BUILD-ACTION-IO-ELEMENT")
        writer.writeBuildActionIoElement(element, obj)

        assert element.find("CATEGORY").text == "ARTIFACT"
        assert element.find("SDGS/SDG") is not None
        assert element.find("ECUC-DEFINITION-REF").text == "/Ecuc/Definition"
        assert element.find("ENGINEERING-OBJECT/FILE-TYPE").text == "c"
        assert element.find("ROLE").text == "input"
        assert element.find("FOREIGN-MODEL-REFERENCE") is None

    def test_write_empty_element(self):
        writer = ARXMLWriter()
        element = ET.Element("BUILD-ACTION-IO-ELEMENT")
        writer.writeBuildActionIoElement(element, BuildActionIoElement())

        assert list(element) == []
