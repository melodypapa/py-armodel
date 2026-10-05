import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    DataPrototypeMapping,
    SubElementMapping,
    TextTableMapping,
)

SPEC_NOTE = (
    "Defines the mapping of two particular VariableDataPrototypes, ParameterDataPrototypes or ArgumentDataPrototypes "
    "with non-equal shortNames, non-equal structure (specific condition is described by [constr_1187]), and/or non-equal "
    "semantic (resolution or range) in context of two different SenderReceiverInterface, NvDataInterface or "
    "ParameterInterface or Operations. If the semantic is unequal, the following rules apply: The textTableMapping is "
    "only applicable if the referred DataPrototypes are typed by AutosarDataType referring to CompuMethods of category "
    "TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE. In the case that the DataPrototypes are typed by "
    "AutosarDataType either referring to CompuMethods of category LINEAR, IDENTICAL or referring to no CompuMethod "
    "(which is similar as IDENTICAL) the linear conversion factor is calculated out of the factorSiToUnit and "
    "offsetSiToUnit attributes of the referred Units and the CompuRationalCoeffs of a compuInternalToPhys of the "
    "referred CompuMethods."
)

FIRST_DATA_NOTE = "First to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation."
SECOND_DATA_NOTE = "Second to be mapped DataPrototype in context of a SenderReceiverInterface, NvDataInterface, ParameterInterface or Operation."
SUB_ELEMENT_NOTE = "This represents the owned SubelementMapping."
TEXT_TABLE_NOTE = "Applied TextTableMapping(s)"


def _ref(value):
    ref = RefType()
    ref.setDest("AUTOSAR-DATA-PROTOTYPE")
    ref.setValue(value)
    return ref


class TestDataPrototypeMapping:
    def test_initialization(self):
        mapping = DataPrototypeMapping()

        assert mapping.getFirstDataPrototypeRef() is None
        assert mapping.getFirstToSecondDataTransformationRef() is None
        assert mapping.getSecondDataPrototypeRef() is None
        assert mapping.getSecondToFirstDataTransformationRef() is None
        assert mapping.getSubElementMappings() == []
        assert mapping.getTextTableMappings() == []

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        mapping = DataPrototypeMapping()
        assert type(mapping).__bases__ == (ARObject,)
        assert isinstance(mapping, ARObject)

    def test_class_docstring_verbatim(self):
        assert DataPrototypeMapping.__doc__.strip() == SPEC_NOTE

    def test_get_set_first_data_prototype_ref(self):
        mapping = DataPrototypeMapping()
        ref = _ref("/Pkg/First")

        result = mapping.setFirstDataPrototypeRef(ref)
        assert result is mapping
        assert mapping.getFirstDataPrototypeRef() is ref
        mapping.setFirstDataPrototypeRef(None)
        assert mapping.getFirstDataPrototypeRef() is ref

    def test_get_set_first_to_second_data_transformation_ref(self):
        mapping = DataPrototypeMapping()
        ref = _ref("/Pkg/Transform")

        result = mapping.setFirstToSecondDataTransformationRef(ref)
        assert result is mapping
        assert mapping.getFirstToSecondDataTransformationRef() is ref
        mapping.setFirstToSecondDataTransformationRef(None)
        assert mapping.getFirstToSecondDataTransformationRef() is ref

    def test_get_set_second_data_prototype_ref(self):
        mapping = DataPrototypeMapping()
        ref = _ref("/Pkg/Second")

        result = mapping.setSecondDataPrototypeRef(ref)
        assert result is mapping
        assert mapping.getSecondDataPrototypeRef() is ref
        mapping.setSecondDataPrototypeRef(None)
        assert mapping.getSecondDataPrototypeRef() is ref

    def test_get_set_second_to_first_data_transformation_ref(self):
        mapping = DataPrototypeMapping()
        ref = _ref("/Pkg/TransformInv")

        result = mapping.setSecondToFirstDataTransformationRef(ref)
        assert result is mapping
        assert mapping.getSecondToFirstDataTransformationRef() is ref
        mapping.setSecondToFirstDataTransformationRef(None)
        assert mapping.getSecondToFirstDataTransformationRef() is ref

    def test_add_sub_element_mapping(self):
        mapping = DataPrototypeMapping()
        sub = SubElementMapping()

        result = mapping.addSubElementMapping(sub)
        assert result is mapping
        assert mapping.getSubElementMappings() == [sub]
        mapping.addSubElementMapping(None)
        assert mapping.getSubElementMappings() == [sub]

    def test_add_text_table_mapping(self):
        mapping = DataPrototypeMapping()
        first = TextTableMapping()
        second = TextTableMapping()

        result = mapping.addTextTableMapping(first)
        assert result is mapping
        mapping.addTextTableMapping(second)
        assert mapping.getTextTableMappings() == [first, second]
        mapping.addTextTableMapping(None)
        assert mapping.getTextTableMappings() == [first, second]

    def test_docstrings_verbatim(self):
        mapping = DataPrototypeMapping()

        def norm(doc):
            return " ".join(doc.split())

        assert norm(mapping.getFirstDataPrototypeRef.__doc__) == FIRST_DATA_NOTE
        assert norm(mapping.setFirstDataPrototypeRef.__doc__) == (FIRST_DATA_NOTE + " A None value is a no-op and does not overwrite an existing firstDataPrototypeRef.")
        assert norm(mapping.getFirstToSecondDataTransformationRef.__doc__).startswith("This reference defines the need to execute the DataTransformation <Mip>_<transformerId> functions")
        assert norm(mapping.getSecondDataPrototypeRef.__doc__) == SECOND_DATA_NOTE
        assert norm(mapping.getSecondToFirstDataTransformationRef.__doc__) == (
            "This defines the need to execute the reverse DataTransformation <Mip>_Inv_<transformerId> functions of "
            "the transformation chain when communicating from the DataPrototypeMapping.secondDataPrototype to the "
            "DataPrototypeMapping.firstDataPrototype."
        )
        assert norm(mapping.addSubElementMapping.__doc__) == (SUB_ELEMENT_NOTE + " A None value is a no-op and does not append anything.")
        assert norm(mapping.getSubElementMappings.__doc__) == SUB_ELEMENT_NOTE
        assert norm(mapping.addTextTableMapping.__doc__) == (TEXT_TABLE_NOTE + " A None value is a no-op and does not append anything.")
        assert norm(mapping.getTextTableMappings.__doc__) == TEXT_TABLE_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(DataPrototypeMapping.getFirstDataPrototypeRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(DataPrototypeMapping.setFirstDataPrototypeRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is DataPrototypeMapping

        hints = typing.get_type_hints(DataPrototypeMapping.getSubElementMappings)
        assert hints.get("return") == typing.List[SubElementMapping]
