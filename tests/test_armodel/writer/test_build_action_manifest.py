"""
Writer tests for BuildActionInvocator (AUTOSAR_FO_TPS_GenericStructureTemplate Table 10.6)
and the BuildActionEntity.invocation dispatch (Table 10.5) that consumes it.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionEntity, BuildActionInvocator, BuildActionIoElement, BuildEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType, RegularExpression, UriString, VerbatimString
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class ConcreteBuildActionEntity(BuildActionEntity):
    pass


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
