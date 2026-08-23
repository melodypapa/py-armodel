"""Writer round-trip tests for LinErrorResponse (Table 3.42, p.97).

Verifies that the singleton wrapper serializes its ``responseErrorRef`` into
a ``LIN-ERROR-RESPONSE`` / ``RESPONSE-ERROR-REF`` element tree and is skipped
when the response is absent.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
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


def test_write_lin_error_response_all_fields(writer):
    parent = _parent()
    response = LinErrorResponse()
    ref = RefType().setValue("/System/ISignalTriggering")
    response.setResponseErrorRef(ref)

    writer.setLinErrorResponse(parent, "LIN-ERROR-RESPONSE", response)

    el = parent.find("LIN-ERROR-RESPONSE")
    assert el is not None
    assert el.find("RESPONSE-ERROR-REF").text == "/System/ISignalTriggering"


def test_write_lin_error_response_none(writer):
    parent = _parent()
    writer.setLinErrorResponse(parent, "LIN-ERROR-RESPONSE", None)
    assert parent.find("LIN-ERROR-RESPONSE") is None
