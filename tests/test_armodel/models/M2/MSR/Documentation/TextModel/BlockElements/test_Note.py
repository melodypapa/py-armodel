"""This module contains tests for the Note module in MSR.Documentation.TextModel.BlockElements."""

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.Note import Note, NoteTypeEnum
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class TestNoteTypeEnum:
    """Test class for NoteTypeEnum class."""

    def test_note_type_enum_members(self):
        """Test that NoteTypeEnum has the expected members."""
        assert NoteTypeEnum.CAUTION == "caution"
        assert NoteTypeEnum.EXAMPLE == "example"
        assert NoteTypeEnum.HINT == "hint"
        assert NoteTypeEnum.OTHER == "other"

    def test_note_type_enum_initialization(self):
        """Test that a NoteTypeEnum object can be initialized."""
        note_type_enum = NoteTypeEnum()
        assert note_type_enum.validateEnumValue("hint")
        assert not note_type_enum.validateEnumValue("unknown")


class TestNote:
    """Test class for Note class."""

    def test_note_initialization(self):
        """Test that a Note object can be initialized with default values."""
        note = Note()
        assert note.label is None
        assert note.noteText is None
        assert note.noteType is None

    def test_note_label_methods(self):
        """Test the label getter and setter."""
        note = Note()
        label = MultilanguageLongName()

        result = note.setLabel(label)
        assert note.getLabel() == label
        assert result == note

        note.setLabel(None)
        assert note.getLabel() == label

    def test_note_note_text_methods(self):
        """Test the noteText getter and setter."""
        note = Note()
        note_text = DocumentationBlock()

        result = note.setNoteText(note_text)
        assert note.getNoteText() == note_text
        assert result == note

        note.setNoteText(None)
        assert note.getNoteText() == note_text

    def test_note_note_type_methods(self):
        """Test the noteType getter and setter."""
        note = Note()
        note_type = NoteTypeEnum()

        result = note.setNoteType(note_type)
        assert note.getNoteType() == note_type
        assert result == note

        note.setNoteType(None)
        assert note.getNoteType() == note_type
