"""Tests for the writePdurIPduGroup handler (R23-11 PdurIPduGroup, Table 6.34, p.352)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.writer.arxml_writer import ARXMLWriter


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


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _string(value):
    s = String()
    s.setValue(value)
    return s


class TestWritePdurIPduGroup:
    """Tests for writePdurIPduGroup handler (R23-11 PdurIPduGroup, Table 6.34, p.352)."""

    def test_children_in_xsd_order(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg")
        group = pkg.createPdurIPduGroup("PduGroup1")
        group.setCommunicationMode(_string("diagnostic"))
        group.addIPduRef(_ref("/System/Ecu1/PduTriggering1", "PDU-TRIGGERING"))
        group.addIPduRef(_ref("/System/Ecu1/PduTriggering2", "PDU-TRIGGERING"))

        parent = _parent()
        writer.writePdurIPduGroup(parent, group)
        child = parent.find("PDUR-I-PDU-GROUP")
        assert child is not None
        assert child.find("SHORT-NAME").text == "PduGroup1"
        assert [c.tag for c in child if c.tag in ("COMMUNICATION-MODE", "I-PDUS")] == ["COMMUNICATION-MODE", "I-PDUS"]
        assert child.find("COMMUNICATION-MODE").text == "diagnostic"
        conditional_tags = child.findall("I-PDUS/PDU-TRIGGERING-REF-CONDITIONAL")
        assert len(conditional_tags) == 2
        assert conditional_tags[0].find("PDU-TRIGGERING-REF").text == "/System/Ecu1/PduTriggering1"
        assert conditional_tags[0].find("PDU-TRIGGERING-REF").get("DEST") == "PDU-TRIGGERING"
        assert conditional_tags[1].find("PDU-TRIGGERING-REF").text == "/System/Ecu1/PduTriggering2"

    def test_empty_children_omitted(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("PdurIPduGroupPkg2")
        group = pkg.createPdurIPduGroup("PduGroup1")
        parent = _parent()
        writer.writePdurIPduGroup(parent, group)
        child = parent.find("PDUR-I-PDU-GROUP")
        assert child is not None
        assert child.find("COMMUNICATION-MODE") is None
        assert child.find("I-PDUS") is None
