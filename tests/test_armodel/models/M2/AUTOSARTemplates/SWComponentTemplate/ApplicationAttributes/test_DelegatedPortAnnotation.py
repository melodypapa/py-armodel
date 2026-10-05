import typing

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DelegatedPortAnnotation,
    SignalFanEnum,
)
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation

CLASS_NOTE = 'Annotation to a "delegated port" to specify the Signal Fan In or Signal Fan Out inside the CompositionSw ComponentType.'
SIGNAL_FAN_NOTE = "Specifies the Signal Fan In or Signal Fan Out inside the Composition Type."


class TestDelegatedPortAnnotation:
    def test_heritage(self):
        assert issubclass(DelegatedPortAnnotation, GeneralAnnotation)

    def test_initialization(self):
        annotation = DelegatedPortAnnotation()

        assert annotation.getSignalFan() is None

    def test_get_set_signal_fan(self):
        annotation = DelegatedPortAnnotation()
        value = SignalFanEnum().setValue(SignalFanEnum.NFOLD)

        assert annotation == annotation.setSignalFan(None)
        assert annotation.getSignalFan() is None

        assert annotation == annotation.setSignalFan(value)
        assert annotation.getSignalFan() is value
        assert annotation.getSignalFan().getValue() == "nfold"

        annotation.setSignalFan(None)
        assert annotation.getSignalFan() is value

    def test_class_docstring_verbatim(self):
        assert DelegatedPortAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert DelegatedPortAnnotation.getSignalFan.__doc__.strip() == SIGNAL_FAN_NOTE
        assert DelegatedPortAnnotation.setSignalFan.__doc__.strip().splitlines()[0] == SIGNAL_FAN_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(DelegatedPortAnnotation.getSignalFan)
        assert hints.get("return") == typing.Optional[SignalFanEnum]

        hints = typing.get_type_hints(DelegatedPortAnnotation.setSignalFan)
        assert hints.get("value") == typing.Optional[SignalFanEnum]
        assert hints.get("return") is DelegatedPortAnnotation
