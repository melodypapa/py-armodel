"""Parser tests for getLinOrderedConfigurableFrame (Table 3.45, p.99).

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinOrderedConfigurableFrame
from tests.test_armodel.parser._helpers import _snip


class TestGetLinOrderedConfigurableFrame:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getLinOrderedConfigurableFrame(element, "LIN-ORDERED-CONFIGURABLE-FRAME")
        assert result is None

    def test_returns_frame_when_child_present(self, parser):
        element = _snip("<LIN-ORDERED-CONFIGURABLE-FRAME>" "<FRAME-REF>/System/LinFrame</FRAME-REF>" "<INDEX>3</INDEX>" "</LIN-ORDERED-CONFIGURABLE-FRAME>")
        result = parser.getLinOrderedConfigurableFrame(element, "LIN-ORDERED-CONFIGURABLE-FRAME")
        assert isinstance(result, LinOrderedConfigurableFrame)
        ref = result.getFrameRef()
        assert isinstance(ref, RefType)
        assert ref.getValue() == "/System/LinFrame"
        assert result.getIndex().getValue() == 3
