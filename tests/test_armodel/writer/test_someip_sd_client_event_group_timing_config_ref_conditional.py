"""Writer round-trip tests for SomeipSdClientEventGroupTimingConfigRefConditional (XSD-only).

Verifies that the singleton wrapper serializes its
SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF into a
``SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL`` element tree and
is skipped when the wrapper is absent.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SomeipSdClientEventGroupTimingConfigRefConditional
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


def _parent():
    return ET.Element("PARENT")


def test_write_ref_conditional_all_fields(writer):
    parent = _parent()
    obj = SomeipSdClientEventGroupTimingConfigRefConditional()
    ref = RefType().setValue("/a/b").setDest("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG")
    obj.setSomeipSdClientEventGroupTimingConfigRef(ref)

    writer.setSomeipSdClientEventGroupTimingConfigRefConditional(parent, "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL", obj)

    el = parent.find("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL")
    assert el is not None
    ref_el = el.find("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF")
    assert ref_el is not None
    assert ref_el.text == "/a/b"
    assert ref_el.attrib["DEST"] == "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG"


def test_write_ref_conditional_none(writer):
    parent = _parent()
    writer.setSomeipSdClientEventGroupTimingConfigRefConditional(parent, "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL", None)
    assert parent.find("SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL") is None
