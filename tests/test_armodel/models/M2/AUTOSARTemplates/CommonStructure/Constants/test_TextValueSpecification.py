import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification, ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, VerbatimString


class TestTextValueSpecification:
    def test_inheritance(self):
        """The purpose of TextValueSpecification is to define the labels that correspond to enumeration values."""
        spec = TextValueSpecification()
        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        """The purpose of TextValueSpecification is to define the labels that correspond to enumeration values."""
        spec = TextValueSpecification()
        assert spec is not None
        assert spec.value is None
        assert spec.shortLabel is None

    def test_value_annotation_is_optional(self):
        """value is a VerbatimString (0..1) attribute — the accessor hints must be Optional[VerbatimString]."""
        hints = typing.get_type_hints(TextValueSpecification.getValue)
        assert hints["return"] == typing.Optional[VerbatimString]
        hints = typing.get_type_hints(TextValueSpecification.setValue)
        assert hints["value"] == typing.Optional[VerbatimString]

    def test_get_value(self):
        """This is the value itself. Note that vt uses the | operator to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod"""
        spec = TextValueSpecification()
        assert spec.getValue() is None

    def test_set_value(self):
        """This is the value itself. Note that vt uses the | operator to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod"""
        spec = TextValueSpecification()
        text = VerbatimString()
        text.setValue("ON")
        result = spec.setValue(text)
        assert result is spec
        assert spec.getValue() is text
        assert spec.getValue().getValue() == "ON"

    def test_set_value_none(self):
        """This is the value itself. Note that vt uses the | operator to separate the values for the different bitfield masks in case that the semantics of the related DataPrototype is described by means of a BITFIELD_TEXTTABLE in the associated CompuMethod"""
        spec = TextValueSpecification()
        text = VerbatimString()
        text.setValue("ON")
        spec.setValue(text)
        result = spec.setValue(None)
        assert result is spec
        assert spec.getValue() is text

    def test_short_label_round_trip(self):
        """This can be used to identify particular value specifications for human readers, for example elements of a record type."""
        spec = TextValueSpecification()
        label = Identifier()
        label.setValue("tvs")
        result = spec.setShortLabel(label)
        assert result is spec
        assert spec.getShortLabel() is label
        result = spec.setShortLabel(None)
        assert result is spec
        assert spec.getShortLabel() is label
