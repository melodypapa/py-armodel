"""Tests for the XrefTarget inline text element."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import XrefTarget


class TestXrefTarget:
    def test_xref_target_initialization(self):
        target = XrefTarget(None, "TARGET")

        assert target.getParent() is None
        assert target.getShortName() == "TARGET"
        assert target.getLongName1() is None
