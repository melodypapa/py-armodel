from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import TransformationDescription, UserDefinedTransformationDescription


class TestUserDefinedTransformationDescription:
    """
    Model tests for UserDefinedTransformationDescription (Table 7.7, p.771).

    Concrete subclass of TransformationDescription (Base = ARObject, Describable,
    TransformationDescription) with zero own attributes.
    """

    def test_class_docstring_is_spec_note_verbatim(self):
        # Table 7.7, p.771 — class Note verbatim from the markdown
        note = "The UserDefinedTransformationDescription is used to specify details and documentation for custom transformers."
        assert UserDefinedTransformationDescription.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert UserDefinedTransformationDescription.__init__.__doc__ is None

    def test_heritage(self):
        assert issubclass(UserDefinedTransformationDescription, TransformationDescription)
        assert issubclass(UserDefinedTransformationDescription, Describable)

        desc = UserDefinedTransformationDescription()
        assert isinstance(desc, TransformationDescription)
        assert isinstance(desc, Describable)

    def test_zero_own_attributes(self):
        # Zero attribute rows (Table 7.7) — no new public accessors beyond the base class
        desc = UserDefinedTransformationDescription()
        base_accessors = {name for name in dir(TransformationDescription) if not name.startswith("_") and callable(getattr(TransformationDescription, name, None))}
        own_accessors = {name for name in dir(desc) if not name.startswith("_") and callable(getattr(desc, name, None))} - base_accessors
        assert own_accessors == set()
