"""Parser tests for SoftwareContext (readSoftwareContext)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import SoftwareContext
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

SOFTWARE_CONTEXT_XML = ("<ROOT xmlns='{ns}'>" "<INPUT>port 4711</INPUT>" "<STATE>WARM_START</STATE>" "</ROOT>").format(ns=NS)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadSoftwareContext:
    def test_read_field_values(self, parser):
        context = SoftwareContext()
        parser.readSoftwareContext(ET.fromstring(SOFTWARE_CONTEXT_XML), context)
        assert context.getInput().getValue() == "port 4711"
        assert context.getState().getValue() == "WARM_START"

    def test_read_absent_children(self, parser):
        context = SoftwareContext()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")
        parser.readSoftwareContext(element, context)
        assert context.getInput() is None
        assert context.getState() is None

    def test_read_partial_children(self, parser):
        context = SoftwareContext()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><STATE>RUNNING</STATE></ROOT>")
        parser.readSoftwareContext(element, context)
        assert context.getState().getValue() == "RUNNING"
        assert context.getInput() is None
