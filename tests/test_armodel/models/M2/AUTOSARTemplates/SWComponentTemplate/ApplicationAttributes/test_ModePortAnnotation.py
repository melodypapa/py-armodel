import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ModePortAnnotation
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation

CLASS_NOTE = "Annotation to a port used for calibration regarding a certain ModeDeclarationGroupPrototype."
MODE_GROUP_NOTE = "The instance of annotated ModeDeclarationGroup Prototype."


class TestModePortAnnotation:
    def test_heritage(self):
        assert issubclass(ModePortAnnotation, GeneralAnnotation)

    def test_initialization(self):
        annotation = ModePortAnnotation()

        assert annotation.getModeGroupRef() is None

    def test_get_set_mode_group_ref(self):
        annotation = ModePortAnnotation()
        ref = RefType().setValue("/Swc/ModeGroup")
        ref.setDest("MODE-DECLARATION-GROUP-PROTOTYPE")

        assert annotation == annotation.setModeGroupRef(None)
        assert annotation.getModeGroupRef() is None

        assert annotation == annotation.setModeGroupRef(ref)
        assert annotation.getModeGroupRef() is ref
        assert annotation.getModeGroupRef().getValue() == "/Swc/ModeGroup"

        annotation.setModeGroupRef(None)
        assert annotation.getModeGroupRef() is ref

    def test_class_docstring_verbatim(self):
        assert ModePortAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert ModePortAnnotation.getModeGroupRef.__doc__.strip() == MODE_GROUP_NOTE
        assert ModePortAnnotation.setModeGroupRef.__doc__.strip().splitlines()[0] == MODE_GROUP_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ModePortAnnotation.getModeGroupRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(ModePortAnnotation.setModeGroupRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is ModePortAnnotation
