"""Parser tests for getSomeipSdClientEventGroupTimingConfigRefConditional (XSD-only).

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import SomeipSdClientEventGroupTimingConfigRefConditional
from tests.test_armodel.parser._helpers import _snip


class TestGetSomeipSdClientEventGroupTimingConfigRefConditional:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getSomeipSdClientEventGroupTimingConfigRefConditional(element, "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL")
        assert result is None

    def test_returns_ref_conditional_when_child_present(self, parser):
        element = _snip(
            "<SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL>"
            '<SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF DEST="SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG">/a/b</SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF>'
            "</SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL>"
        )
        result = parser.getSomeipSdClientEventGroupTimingConfigRefConditional(element, "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL")
        assert isinstance(result, SomeipSdClientEventGroupTimingConfigRefConditional)
        ref = result.getSomeipSdClientEventGroupTimingConfigRef()
        assert ref is not None
        assert ref.getValue() == "/a/b"
