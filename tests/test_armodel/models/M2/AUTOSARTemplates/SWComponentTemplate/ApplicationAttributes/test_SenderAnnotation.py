
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    SenderAnnotation,
    SenderReceiverAnnotation,
)

CLASS_NOTE = "Annotation of a sender port, specifying properties of data elements that don't affect communication or generation of the RTE."


class TestSenderAnnotation:
    def test_heritage(self):
        annotation = SenderAnnotation()

        assert isinstance(annotation, SenderReceiverAnnotation)
        assert type(annotation).__bases__ == (SenderReceiverAnnotation,)

    def test_instantiable(self):
        SenderAnnotation()

    def test_class_docstring_verbatim(self):
        assert SenderAnnotation.__doc__.strip() == CLASS_NOTE

    def test_base_properties_accessible(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

        annotation = SenderAnnotation()
        value = Boolean().setValue(True)
        annotation.setComputed(value)
        assert annotation.getComputed() is value
