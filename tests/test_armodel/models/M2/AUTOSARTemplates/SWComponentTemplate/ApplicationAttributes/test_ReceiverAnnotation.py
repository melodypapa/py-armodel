import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ReceiverAnnotation, SenderReceiverAnnotation

CLASS_NOTE = (
    "Annotation of a receiver port, specifying properties of data elements that don't affect communication or generation of the RTE. The given attributes are requirements on the required data."
)
SIGNAL_AGE_NOTE = "The maximum allowed age of the signal since it was originally read by a sensor. This is a requirement specified on the receiver side."


class TestReceiverAnnotation:
    def test_heritage(self):
        annotation = ReceiverAnnotation()

        assert isinstance(annotation, SenderReceiverAnnotation)
        assert type(annotation).__bases__ == (SenderReceiverAnnotation,)

    def test_initialization(self):
        annotation = ReceiverAnnotation()

        assert annotation.getSignalAge() is None

    def test_get_set_signal_age(self):
        annotation = ReceiverAnnotation()
        value = MultidimensionalTime()

        assert annotation == annotation.setSignalAge(None)
        assert annotation.getSignalAge() is None

        assert annotation == annotation.setSignalAge(value)
        assert annotation.getSignalAge() is value

        annotation.setSignalAge(None)
        assert annotation.getSignalAge() is value

    def test_class_docstring_verbatim(self):
        assert ReceiverAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert ReceiverAnnotation.getSignalAge.__doc__.strip() == SIGNAL_AGE_NOTE
        assert ReceiverAnnotation.setSignalAge.__doc__.strip().splitlines()[0] == SIGNAL_AGE_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ReceiverAnnotation.getSignalAge)
        assert hints.get("return") == typing.Optional[MultidimensionalTime]

        hints = typing.get_type_hints(ReceiverAnnotation.setSignalAge)
        assert hints.get("value") == typing.Optional[MultidimensionalTime]
        assert hints.get("return") is ReceiverAnnotation
