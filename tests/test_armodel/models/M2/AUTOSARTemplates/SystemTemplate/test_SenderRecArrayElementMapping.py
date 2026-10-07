import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    IndexedArrayElement,
    SenderRecArrayElementMapping,
    SenderRecArrayTypeMapping,
    SenderRecCompositeTypeMapping,
    SenderRecRecordTypeMapping,
)


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestSenderRecArrayElementMapping:
    """Test cases for SenderRecArrayElementMapping (Table 5.31, p.237)."""

    MEMBERS = [
        "complexTypeMapping",
        "indexedArrayElement",
        "systemSignalRef",
    ]

    def test_inheritance(self):
        assert issubclass(SenderRecArrayElementMapping, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "The SenderRecArrayElement may be a primitive one or a composite one. "
            "If the element is primitive, it will be mapped to the SystemSignal (multiplicity 1). "
            "If the VariableDataPrototype that is referenced by Sender ReceiverToSignalGroupMapping is typed by an ApplicationDataType "
            "the reference to the Application ArrayElement shall be used. "
            "If the VariableDataPrototype is typed by the ImplementationData"
        )
        doc = inspect.cleandoc(SenderRecArrayElementMapping.__doc__)
        assert doc.startswith(expected)

    def test_init_has_no_docstring(self):
        assert SenderRecArrayElementMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = SenderRecArrayElementMapping()
        assert mapping.getComplexTypeMapping() is None
        assert mapping.getIndexedArrayElement() is None
        assert mapping.getSystemSignalRef() is None

    def test_member_order(self):
        mapping = SenderRecArrayElementMapping()
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_complex_type_mapping(self):
        mapping = SenderRecArrayElementMapping()
        type_mapping = SenderRecArrayTypeMapping()
        result = mapping.setComplexTypeMapping(type_mapping)
        assert result is mapping
        assert mapping.getComplexTypeMapping() is type_mapping
        assert isinstance(mapping.getComplexTypeMapping(), SenderRecCompositeTypeMapping)
        record_type_mapping = SenderRecRecordTypeMapping()
        mapping.setComplexTypeMapping(record_type_mapping)
        assert mapping.getComplexTypeMapping() is record_type_mapping
        mapping.setComplexTypeMapping(None)
        assert mapping.getComplexTypeMapping() is record_type_mapping

    def test_get_set_indexed_array_element(self):
        mapping = SenderRecArrayElementMapping()
        indexed = IndexedArrayElement()
        index = Integer()
        index.setValue(2)
        indexed.setIndex(index)
        result = mapping.setIndexedArrayElement(indexed)
        assert result is mapping
        assert mapping.getIndexedArrayElement() is indexed
        mapping.setIndexedArrayElement(None)
        assert mapping.getIndexedArrayElement() is indexed

    def test_get_set_system_signal_ref(self):
        mapping = SenderRecArrayElementMapping()
        result = mapping.setSystemSignalRef(_ref("/SystemSignal"))
        assert result is mapping
        assert mapping.getSystemSignalRef().getValue() == "/SystemSignal"
        mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef().getValue() == "/SystemSignal"

    def test_type_hints(self):
        hints = typing.get_type_hints(SenderRecArrayElementMapping.getComplexTypeMapping)
        assert hints["return"] == typing.Optional[SenderRecCompositeTypeMapping]
        hints = typing.get_type_hints(SenderRecArrayElementMapping.setComplexTypeMapping)
        assert hints["value"] == typing.Optional[SenderRecCompositeTypeMapping]
        assert hints["return"] is SenderRecArrayElementMapping
        hints = typing.get_type_hints(SenderRecArrayElementMapping.getIndexedArrayElement)
        assert hints["return"] == typing.Optional[IndexedArrayElement]
        hints = typing.get_type_hints(SenderRecArrayElementMapping.setIndexedArrayElement)
        assert hints["value"] == typing.Optional[IndexedArrayElement]
        assert hints["return"] is SenderRecArrayElementMapping
        hints = typing.get_type_hints(SenderRecArrayElementMapping.getSystemSignalRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SenderRecArrayElementMapping.setSystemSignalRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is SenderRecArrayElementMapping
