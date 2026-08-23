"""Parser tests for getLinConfigurableFrame (Table 3.44, p.99).

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinConfigurableFrame
from tests.test_armodel.parser._helpers import _snip


class TestGetLinConfigurableFrame:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getLinConfigurableFrame(element, "LIN-CONFIGURABLE-FRAME")
        assert result is None

    def test_returns_frame_when_child_present(self, parser):
        element = _snip("<LIN-CONFIGURABLE-FRAME>" "<FRAME-REF>/System/LinFrame</FRAME-REF>" "<MESSAGE-ID>42</MESSAGE-ID>" "</LIN-CONFIGURABLE-FRAME>")
        result = parser.getLinConfigurableFrame(element, "LIN-CONFIGURABLE-FRAME")
        assert isinstance(result, LinConfigurableFrame)
        ref = result.getFrameRef()
        assert isinstance(ref, RefType)
        assert ref.getValue() == "/System/LinFrame"
        assert result.getMessageId().getValue() == 42
