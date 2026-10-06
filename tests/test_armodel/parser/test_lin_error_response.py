"""Parser tests for getLinErrorResponse (Table 3.42, p.97).

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from tests.test_armodel.parser._helpers import _snip


class TestGetLinErrorResponse:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getLinErrorResponse(element, "LIN-ERROR-RESPONSE")
        assert result is None

    def test_returns_response_when_child_present(self, parser):
        element = _snip("<LIN-ERROR-RESPONSE>" "<RESPONSE-ERROR-REF>/System/ISignalTriggering</RESPONSE-ERROR-REF>" "</LIN-ERROR-RESPONSE>")
        result = parser.getLinErrorResponse(element, "LIN-ERROR-RESPONSE")
        assert isinstance(result, LinErrorResponse)
        ref = result.getResponseErrorRef()
        assert isinstance(ref, RefType)
        assert ref.getValue() == "/System/ISignalTriggering"

    def test_reads_checksum_and_timestamp_attributes(self, parser):
        element = _snip('<LIN-ERROR-RESPONSE S="1234" T="2024-01-01T00:00:00Z">' "<RESPONSE-ERROR-REF>/System/ISignalTriggering</RESPONSE-ERROR-REF>" "</LIN-ERROR-RESPONSE>")
        result = parser.getLinErrorResponse(element, "LIN-ERROR-RESPONSE")

        assert isinstance(result, LinErrorResponse)
        assert result.getChecksum() is not None
        assert result.getChecksum().getValue() == "1234"
        assert result.getTimestamp() is not None
        assert result.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_reads_empty_wrapper_to_default_field(self, parser):
        element = _snip("<LIN-ERROR-RESPONSE/>")
        result = parser.getLinErrorResponse(element, "LIN-ERROR-RESPONSE")

        assert isinstance(result, LinErrorResponse)
        assert result.getResponseErrorRef() is None
