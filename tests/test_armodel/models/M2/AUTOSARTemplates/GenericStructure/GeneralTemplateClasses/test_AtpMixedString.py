import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString


class _Mixed(AtpMixedString):
    def __init__(self):
        super().__init__()


def test_abstract_guard():
    with pytest.raises(TypeError):
        AtpMixedString()


def test_default_none_and_round_trip():
    m = _Mixed()
    assert m.getMixedString() is None
    assert m.setMixedString("A and\n B ").getMixedString() == "A and\n B "
    assert isinstance(m, AtpMixedString)


def test_none_noop_and_chaining():
    m = _Mixed()
    m.setMixedString("keep")
    assert m.setMixedString(None) is m
    assert m.getMixedString() == "keep"
