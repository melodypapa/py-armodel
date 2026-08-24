"""Parser tests for getCanXlFrameTriggeringProps (Table F.27, p.447).

Shared fixtures (``parser``) are provided by ``conftest.py``; the ``_snip``
helper lives in ``_helpers.py``.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import CanXlFrameTriggeringProps
from tests.test_armodel.parser._helpers import _snip


class TestGetCanXlFrameTriggeringProps:
    def test_returns_none_when_child_absent(self, parser):
        element = _snip("<OTHER/>")
        result = parser.getCanXlFrameTriggeringProps(element, "CAN-XL-FRAME-TRIGGERING-PROPS")
        assert result is None

    def test_returns_props_when_child_present(self, parser):
        element = _snip(
            "<CAN-XL-FRAME-TRIGGERING-PROPS>" "<ACCEPTANCE-FIELD>0</ACCEPTANCE-FIELD>" "<PRIORITY-ID>7</PRIORITY-ID>" "<SDU-TYPE>8</SDU-TYPE>" "<VCID>10</VCID>" "</CAN-XL-FRAME-TRIGGERING-PROPS>"
        )
        result = parser.getCanXlFrameTriggeringProps(element, "CAN-XL-FRAME-TRIGGERING-PROPS")
        assert isinstance(result, CanXlFrameTriggeringProps)
        acceptance = result.getAcceptanceField()
        assert isinstance(acceptance, PositiveInteger)
        assert acceptance.getValue() == 0
        assert result.getPriorityId().getValue() == 7
        assert result.getSduType().getValue() == 8
        assert result.getVcid().getValue() == 10
