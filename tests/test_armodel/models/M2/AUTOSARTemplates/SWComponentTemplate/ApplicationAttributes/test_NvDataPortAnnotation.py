import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import NvDataPortAnnotation
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation

CLASS_NOTE = "Annotation to a port regarding a certain VariableDataPrototype."
VARIABLE_NOTE = "The instance of nv data annotated."


class TestNvDataPortAnnotation:
    def test_heritage(self):
        assert issubclass(NvDataPortAnnotation, GeneralAnnotation)

    def test_initialization(self):
        annotation = NvDataPortAnnotation()

        assert annotation.getVariableRef() is None

    def test_get_set_variable_ref(self):
        annotation = NvDataPortAnnotation()
        ref = RefType().setValue("/Swc/Nv")
        ref.setDest("VARIABLE-DATA-PROTOTYPE")

        assert annotation == annotation.setVariableRef(None)
        assert annotation.getVariableRef() is None

        assert annotation == annotation.setVariableRef(ref)
        assert annotation.getVariableRef() is ref
        assert annotation.getVariableRef().getValue() == "/Swc/Nv"

        annotation.setVariableRef(None)
        assert annotation.getVariableRef() is ref

    def test_class_docstring_verbatim(self):
        assert NvDataPortAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert NvDataPortAnnotation.getVariableRef.__doc__.strip() == VARIABLE_NOTE
        assert NvDataPortAnnotation.setVariableRef.__doc__.strip().splitlines()[0] == VARIABLE_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(NvDataPortAnnotation.getVariableRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(NvDataPortAnnotation.setVariableRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is NvDataPortAnnotation
