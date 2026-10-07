import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    DataMapping,
    SenderRecCompositeTypeMapping,
    SenderReceiverCompositeElementToSignalMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestSenderReceiverCompositeElementToSignalMapping:
    """Test cases for SenderReceiverCompositeElementToSignalMapping (Table 5.34, p.247)."""

    MEMBERS = [
        "dataElementIRef",
        "systemSignalRef",
        "typeMapping",
    ]

    def test_inheritance(self):
        assert issubclass(SenderReceiverCompositeElementToSignalMapping, DataMapping)

    def test_class_docstring_note(self):
        expected = "Mapping of an Variable Data Prototype which is aggregated within a composite datatype to a System Signal (only one element of the composite data type is mapped)."
        assert inspect.cleandoc(SenderReceiverCompositeElementToSignalMapping.__doc__).split("\n\n")[0] == expected

    def test_init_has_no_docstring(self):
        assert SenderReceiverCompositeElementToSignalMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = SenderReceiverCompositeElementToSignalMapping()
        assert mapping.getDataElementIRef() is None
        assert mapping.getSystemSignalRef() is None
        assert mapping.getTypeMapping() is None

    def test_member_order(self):
        mapping = SenderReceiverCompositeElementToSignalMapping()
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_data_element_i_ref(self):
        mapping = SenderReceiverCompositeElementToSignalMapping()
        iref = VariableDataPrototypeInSystemInstanceRef()
        result = mapping.setDataElementIRef(iref)
        assert result is mapping
        assert mapping.getDataElementIRef() is iref
        mapping.setDataElementIRef(None)
        assert mapping.getDataElementIRef() is iref

    def test_get_set_system_signal_ref(self):
        mapping = SenderReceiverCompositeElementToSignalMapping()
        result = mapping.setSystemSignalRef(_ref("/System/Signal"))
        assert result is mapping
        assert mapping.getSystemSignalRef().getValue() == "/System/Signal"
        mapping.setSystemSignalRef(None)
        assert mapping.getSystemSignalRef().getValue() == "/System/Signal"

    def test_get_set_type_mapping(self):
        mapping = SenderReceiverCompositeElementToSignalMapping()
        type_mapping = SenderRecRecordTypeMapping()
        result = mapping.setTypeMapping(type_mapping)
        assert result is mapping
        assert mapping.getTypeMapping() is type_mapping
        assert isinstance(mapping.getTypeMapping(), SenderRecCompositeTypeMapping)
        mapping.setTypeMapping(None)
        assert mapping.getTypeMapping() is type_mapping

    def test_type_hints(self):
        hints = typing.get_type_hints(SenderReceiverCompositeElementToSignalMapping.getDataElementIRef)
        assert hints["return"] == typing.Optional[VariableDataPrototypeInSystemInstanceRef]
        hints = typing.get_type_hints(SenderReceiverCompositeElementToSignalMapping.setDataElementIRef)
        assert hints["value"] == typing.Optional[VariableDataPrototypeInSystemInstanceRef]
        assert hints["return"] is SenderReceiverCompositeElementToSignalMapping
        hints = typing.get_type_hints(SenderReceiverCompositeElementToSignalMapping.getSystemSignalRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(SenderReceiverCompositeElementToSignalMapping.setSystemSignalRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is SenderReceiverCompositeElementToSignalMapping
        hints = typing.get_type_hints(SenderReceiverCompositeElementToSignalMapping.getTypeMapping)
        assert hints["return"] == typing.Optional[SenderRecCompositeTypeMapping]
        hints = typing.get_type_hints(SenderReceiverCompositeElementToSignalMapping.setTypeMapping)
        assert hints["value"] == typing.Optional[SenderRecCompositeTypeMapping]
        assert hints["return"] is SenderReceiverCompositeElementToSignalMapping
