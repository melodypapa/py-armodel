"""
Writer tests for BuildActionInvocator (AUTOSAR_FO_TPS_GenericStructureTemplate Table 10.6)
and the BuildActionEntity.invocation dispatch (Table 10.5) that consumes it.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionEntity, BuildActionInvocator
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
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
