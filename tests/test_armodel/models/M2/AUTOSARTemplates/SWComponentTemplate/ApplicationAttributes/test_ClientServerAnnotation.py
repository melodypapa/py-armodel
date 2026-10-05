import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import ClientServerAnnotation

CLASS_NOTE = "Annotation to a port regarding a certain Operation."
OPERATION_NOTE = "This represents the ClientServerOperation that the Client ServerAnnotation corresponds to."


class TestClientServerAnnotation:
    def test_initialization(self):
        annotation = ClientServerAnnotation()

        assert annotation.getOperationRef() is None

    def test_get_set_operation_ref(self):
        annotation = ClientServerAnnotation()
        ref = RefType().setValue("/If/Op")
        ref.setDest("CLIENT-SERVER-OPERATION")

        assert annotation == annotation.setOperationRef(None)
        assert annotation.getOperationRef() is None

        assert annotation == annotation.setOperationRef(ref)
        assert annotation.getOperationRef() is ref
        assert annotation.getOperationRef().getValue() == "/If/Op"

        annotation.setOperationRef(None)
        assert annotation.getOperationRef() is ref

    def test_class_docstring_verbatim(self):
        assert ClientServerAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert ClientServerAnnotation.getOperationRef.__doc__.strip() == OPERATION_NOTE
        assert ClientServerAnnotation.setOperationRef.__doc__.strip().splitlines()[0] == OPERATION_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(ClientServerAnnotation.getOperationRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(ClientServerAnnotation.setOperationRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is ClientServerAnnotation
