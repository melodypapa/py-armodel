import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Numerical
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableValuePair

SPEC_NOTE = "Defines a pair of text values which are translated into each other."
VALUE_NOTE = (
    "Value of first DataPrototype provided similar to a numerical ValueSpecification which is intended to be "
    "assigned to a Primitive data element. Note that the numerical value is a variant, it can be computed by a formula."
)


class TestTextTableValuePair:
    def test_initialization(self):
        value_pair = TextTableValuePair()

        assert value_pair.getFirstValue() is None
        assert value_pair.getSecondValue() is None

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        value_pair = TextTableValuePair()
        assert type(value_pair).__bases__ == (ARObject,)
        assert isinstance(value_pair, ARObject)

    def test_class_docstring_verbatim(self):
        assert TextTableValuePair.__doc__.strip() == SPEC_NOTE

    def test_get_set_first_value(self):
        value_pair = TextTableValuePair()
        value = Numerical()
        value.setValue("1")

        result = value_pair.setFirstValue(value)
        assert result is value_pair
        assert value_pair.getFirstValue() is value
        value_pair.setFirstValue(None)
        assert value_pair.getFirstValue() is value

    def test_get_set_second_value(self):
        value_pair = TextTableValuePair()
        value = Numerical()
        value.setValue("2")

        result = value_pair.setSecondValue(value)
        assert result is value_pair
        assert value_pair.getSecondValue() is value
        value_pair.setSecondValue(None)
        assert value_pair.getSecondValue() is value

    def test_docstrings_verbatim(self):
        value_pair = TextTableValuePair()

        def norm(doc):
            return " ".join(doc.split())

        assert norm(value_pair.getFirstValue.__doc__) == VALUE_NOTE
        assert norm(value_pair.setFirstValue.__doc__) == (VALUE_NOTE + " A None value is a no-op and does not overwrite an existing firstValue.")
        assert norm(value_pair.getSecondValue.__doc__).startswith("Value of second DataPrototype provided similar to a numerical")
        assert "A None value is a no-op and does not overwrite an existing secondValue." in norm(value_pair.setSecondValue.__doc__)

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(TextTableValuePair.getFirstValue)
        assert hints.get("return") == typing.Optional[Numerical]

        hints = typing.get_type_hints(TextTableValuePair.setSecondValue)
        assert hints.get("value") == typing.Optional[Numerical]
        assert hints.get("return") is TextTableValuePair
