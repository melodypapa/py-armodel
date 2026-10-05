import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import TriggerPortAnnotation
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation

CLASS_NOTE = "Annotation to a port used for calibration regarding a certain Trigger."
TRIGGER_NOTE = "The instance of annotated trigger."


class TestTriggerPortAnnotation:
    def test_heritage(self):
        assert issubclass(TriggerPortAnnotation, GeneralAnnotation)

    def test_initialization(self):
        annotation = TriggerPortAnnotation()

        assert annotation.getTriggerRef() is None

    def test_get_set_trigger_ref(self):
        annotation = TriggerPortAnnotation()
        ref = RefType().setValue("/Swc/Trigger")
        ref.setDest("TRIGGER")

        assert annotation == annotation.setTriggerRef(None)
        assert annotation.getTriggerRef() is None

        assert annotation == annotation.setTriggerRef(ref)
        assert annotation.getTriggerRef() is ref
        assert annotation.getTriggerRef().getValue() == "/Swc/Trigger"

        annotation.setTriggerRef(None)
        assert annotation.getTriggerRef() is ref

    def test_class_docstring_verbatim(self):
        assert TriggerPortAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert TriggerPortAnnotation.getTriggerRef.__doc__.strip() == TRIGGER_NOTE
        assert TriggerPortAnnotation.setTriggerRef.__doc__.strip().splitlines()[0] == TRIGGER_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(TriggerPortAnnotation.getTriggerRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(TriggerPortAnnotation.setTriggerRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is TriggerPortAnnotation
