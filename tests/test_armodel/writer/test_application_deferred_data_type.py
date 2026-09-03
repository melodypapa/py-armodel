"""Writer tests for ApplicationDeferredDataType (R23-11 Table 3.17)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("ELEMENTS")


class TestApplicationDeferredDataTypeWriter:

    def test_write_application_deferred_data_type(self, writer):
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("AppPkg")
        data_type = pkg.createApplicationDeferredDataType("MyDeferred")

        parent = _parent()
        writer.writeApplicationDeferredDataType(parent, data_type)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "APPLICATION-DEFERRED-DATA-TYPE"
        assert child.find("SHORT-NAME").text == "MyDeferred"
