"""
This module contains comprehensive tests for the IncludedDataTypes module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the IncludedDataTypes.py file to achieve 100% test coverage.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet

CLASS_NOTE = (
    "An includedDataTypeSet declares that a set of AutosarDataType is used by a basic software module or a software component for its implementation and the AutosarDataType becomes part of the contract. "  # noqa E501
    "This information is required if the AutosarDataType is not used for any DataPrototype owned by this software component or if the enumeration literals, lowerLimit and upperLimit constants shall be generated with a literalPrefix. "  # noqa E501
    "The optional literalPrefix is used to add a common prefix on enumeration literals, lowerLimit and upper Limit constants created by the RTE."  # noqa E501
)

DATA_TYPE_NOTE = "AutosarDataType belonging to the includedDataTypeSet"

LITERAL_PREFIX_NOTE = "LiteralPrefix defines a common prefix for all AutosarData Types of the includedDataTypeSet to be added on enumeration literals, lowerLimit and upperLimit constants created by the RTE."  # noqa E501


class TestIncludedDataTypeSet:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 7.50)"""
        assert IncludedDataTypeSet.__doc__.strip() == CLASS_NOTE
        assert IncludedDataTypeSet.addDataTypeRef.__doc__.strip() == (DATA_TYPE_NOTE + " A None value is a no-op and does not append to dataTypeRefs.")
        assert IncludedDataTypeSet.getDataTypeRefs.__doc__.strip() == DATA_TYPE_NOTE
        assert IncludedDataTypeSet.getLiteralPrefix.__doc__.strip() == LITERAL_PREFIX_NOTE
        assert IncludedDataTypeSet.setLiteralPrefix.__doc__.strip() == (LITERAL_PREFIX_NOTE + " A None value is a no-op and does not overwrite an existing literalPrefix.")

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        assert issubclass(IncludedDataTypeSet, ARObject)
        included_data_type_set = IncludedDataTypeSet()
        assert included_data_type_set.dataTypeRefs == []
        assert included_data_type_set.literalPrefix is None

        hints = typing.get_type_hints(IncludedDataTypeSet.addDataTypeRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is IncludedDataTypeSet
        hints = typing.get_type_hints(IncludedDataTypeSet.getDataTypeRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(IncludedDataTypeSet.getLiteralPrefix)
        assert hints["return"] == typing.Optional[Identifier]
        hints = typing.get_type_hints(IncludedDataTypeSet.setLiteralPrefix)
        assert hints["value"] == typing.Optional[Identifier]
        assert hints["return"] is IncludedDataTypeSet

    def test_initialization(self):
        """Test IncludedDataTypeSet initialization"""
        included_data_type_set = IncludedDataTypeSet()

        assert included_data_type_set is not None
        assert included_data_type_set.dataTypeRefs == []
        assert included_data_type_set.literalPrefix is None

    def test_add_get_data_type_refs(self):
        """Test addDataTypeRef and getDataTypeRefs methods"""
        included_data_type_set = IncludedDataTypeSet()

        assert included_data_type_set.getDataTypeRefs() == []

        ref = RefType()
        ref.setValue("/AutosarTypes/DataType")
        result = included_data_type_set.addDataTypeRef(ref)
        assert result is included_data_type_set  # Method chaining
        assert ref in included_data_type_set.getDataTypeRefs()
        assert included_data_type_set.getDataTypeRefs() == [ref]

        # None is a no-op
        included_data_type_set.addDataTypeRef(None)
        assert included_data_type_set.getDataTypeRefs() == [ref]

    def test_get_set_literal_prefix(self):
        """Test getLiteralPrefix and setLiteralPrefix methods"""
        included_data_type_set = IncludedDataTypeSet()

        assert included_data_type_set.getLiteralPrefix() is None

        prefix = Identifier()
        prefix.setValue("myPrefix")
        result = included_data_type_set.setLiteralPrefix(prefix)
        assert result is included_data_type_set  # Method chaining
        assert included_data_type_set.getLiteralPrefix() == prefix

        # None is a no-op
        included_data_type_set.setLiteralPrefix(None)
        assert included_data_type_set.getLiteralPrefix() == prefix
