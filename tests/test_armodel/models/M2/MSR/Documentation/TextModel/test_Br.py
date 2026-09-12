"""Tests for the Br inline text element."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br


class TestBr:
    def test_br_initialization(self):
        br = Br()

        assert br.parent is None
        assert br.getChecksum() is None
        assert br.getTimestamp() is None
