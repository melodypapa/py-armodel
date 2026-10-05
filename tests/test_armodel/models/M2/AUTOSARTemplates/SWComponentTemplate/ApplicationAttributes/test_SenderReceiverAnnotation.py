import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    DataLimitKindEnum,
    ProcessingKindEnum,
    ReceiverAnnotation,
    SenderAnnotation,
    SenderReceiverAnnotation,
)

CLASS_NOTE = "Annotation of the data elements in a port that realizes a sender/receiver interface."
COMPUTED_NOTE = "Flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values."
DATA_ELEMENT_NOTE = "The instance of VariableDataPrototype annotated."
LIMIT_KIND_NOTE = "This min or max has not to be mismatched with the min- and max for data-value in a compu-method. For example, this annotation shows when the result of the calculation performed in a RunnableEntity owned by one AtomicSwComponentType is transmitted to another AtomicSwComponentType whose RunnableEntity will use this value as a limit, e.g. the max.power which can be used by that software-component, or the current min. slip."
PROCESSING_KIND_NOTE = "This attribute controls how data is processed according to the possible values of ProcessingKindEnum."


class TestSenderReceiverAnnotation:
    def test_abstract_guard(self):
        with pytest.raises(TypeError):
            SenderReceiverAnnotation()

    def test_concrete_subclasses_inherit_base(self):
        sender = SenderAnnotation()
        assert isinstance(sender, SenderReceiverAnnotation)
        receiver = ReceiverAnnotation()
        assert isinstance(receiver, SenderReceiverAnnotation)

    def test_base_properties_via_concrete_subclass(self):
        annotation = ReceiverAnnotation()

        assert annotation.getComputed() is None
        assert annotation.getDataElementRef() is None
        assert annotation.getLimitKind() is None
        assert annotation.getProcessingKind() is None

    def test_get_set_computed(self):
        annotation = ReceiverAnnotation()
        value = Boolean().setValue(True)

        assert annotation == annotation.setComputed(None)
        assert annotation.getComputed() is None

        assert annotation == annotation.setComputed(value)
        assert annotation.getComputed() is value
        assert annotation.getComputed().getValue() is True

        annotation.setComputed(None)
        assert annotation.getComputed() is value

    def test_get_set_data_element_ref(self):
        annotation = ReceiverAnnotation()
        ref = RefType().setValue("/Pkg/DataElement")

        assert annotation == annotation.setDataElementRef(None)
        assert annotation.getDataElementRef() is None

        assert annotation == annotation.setDataElementRef(ref)
        assert annotation.getDataElementRef() is ref
        assert annotation.getDataElementRef().getValue() == "/Pkg/DataElement"

        annotation.setDataElementRef(None)
        assert annotation.getDataElementRef() is ref

    def test_get_set_limit_kind(self):
        annotation = ReceiverAnnotation()
        value = DataLimitKindEnum().setValue(DataLimitKindEnum.MAX)

        assert annotation == annotation.setLimitKind(None)
        assert annotation.getLimitKind() is None

        assert annotation == annotation.setLimitKind(value)
        assert annotation.getLimitKind() is value
        assert annotation.getLimitKind().getValue() == "max"

        annotation.setLimitKind(None)
        assert annotation.getLimitKind() is value

    def test_get_set_processing_kind(self):
        annotation = ReceiverAnnotation()
        value = ProcessingKindEnum().setValue(ProcessingKindEnum.FILTERED)

        assert annotation == annotation.setProcessingKind(None)
        assert annotation.getProcessingKind() is None

        assert annotation == annotation.setProcessingKind(value)
        assert annotation.getProcessingKind() is value
        assert annotation.getProcessingKind().getValue() == "filtered"

        annotation.setProcessingKind(None)
        assert annotation.getProcessingKind() is value

    def test_class_docstring_verbatim(self):
        assert SenderReceiverAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert SenderReceiverAnnotation.getComputed.__doc__.strip() == COMPUTED_NOTE
        assert SenderReceiverAnnotation.setComputed.__doc__.strip().splitlines()[0] == COMPUTED_NOTE
        assert SenderReceiverAnnotation.getDataElementRef.__doc__.strip() == DATA_ELEMENT_NOTE
        assert SenderReceiverAnnotation.setDataElementRef.__doc__.strip().splitlines()[0] == DATA_ELEMENT_NOTE
        assert SenderReceiverAnnotation.getLimitKind.__doc__.strip() == LIMIT_KIND_NOTE
        assert SenderReceiverAnnotation.setLimitKind.__doc__.strip().splitlines()[0] == LIMIT_KIND_NOTE
        assert SenderReceiverAnnotation.getProcessingKind.__doc__.strip() == PROCESSING_KIND_NOTE
        assert SenderReceiverAnnotation.setProcessingKind.__doc__.strip().splitlines()[0] == PROCESSING_KIND_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(SenderReceiverAnnotation.getComputed)
        assert hints.get("return") == typing.Optional[Boolean]

        hints = typing.get_type_hints(SenderReceiverAnnotation.setComputed)
        assert hints.get("value") == typing.Optional[Boolean]
        assert hints.get("return") is SenderReceiverAnnotation

        hints = typing.get_type_hints(SenderReceiverAnnotation.getDataElementRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(SenderReceiverAnnotation.setDataElementRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is SenderReceiverAnnotation

        hints = typing.get_type_hints(SenderReceiverAnnotation.getLimitKind)
        assert hints.get("return") == typing.Optional[DataLimitKindEnum]

        hints = typing.get_type_hints(SenderReceiverAnnotation.getProcessingKind)
        assert hints.get("return") == typing.Optional[ProcessingKindEnum]
