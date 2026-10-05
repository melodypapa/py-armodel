import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ParameterPortAnnotation
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation

CLASS_NOTE = "Annotation to a port used for calibration regarding a certain ParameterDataPrototype."
PARAMETER_NOTE = "The instance of annotated ParameterDataPrototype."


class TestParameterPortAnnotation:
    def test_heritage(self):
        assert issubclass(ParameterPortAnnotation, GeneralAnnotation)

    def test_initialization(self):
        annotation = ParameterPortAnnotation()

        assert annotation.getParameterRef() is None

    def test_get_set_parameter_ref(self):
        annotation = ParameterPortAnnotation()
        ref = RefType().setValue("/Swc/Param")
        ref.setDest("PARAMETER-DATA-PROTOTYPE")

        assert annotation == annotation.setParameterRef(None)
        assert annotation.getParameterRef() is None

        assert annotation == annotation.setParameterRef(ref)
        assert annotation.getParameterRef() is ref
        assert annotation.getParameterRef().getValue() == "/Swc/Param"

        annotation.setParameterRef(None)
        assert annotation.getParameterRef() is ref

    def test_class_docstring_verbatim(self):
        assert ParameterPortAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert ParameterPortAnnotation.getParameterRef.__doc__.strip() == PARAMETER_NOTE
        assert ParameterPortAnnotation.setParameterRef.__doc__.strip().splitlines()[0] == PARAMETER_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ParameterPortAnnotation.getParameterRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(ParameterPortAnnotation.setParameterRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is ParameterPortAnnotation
