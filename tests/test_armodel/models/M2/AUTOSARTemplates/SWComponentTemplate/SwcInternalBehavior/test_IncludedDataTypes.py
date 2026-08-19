"""
This module contains comprehensive tests for the IncludedDataTypes module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the IncludedDataTypes.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet


class TestIncludedDataTypeSet:
    """Test class for IncludedDataTypeSet class."""

    def test_included_data_type_set_initialization(self):
        """Test IncludedDataTypeSet initialization and methods."""
        set = IncludedDataTypeSet()

        assert set.dataTypeRefs == []
        assert set.literalPrefix is None

        # Test dataTypeRefs methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = RefType()
        ref.setValue("/Test/Ref")
        set.addDataTypeRef(ref)
        assert ref in set.getDataTypeRefs()

        # Test addDataTypeRef with None
        set.addDataTypeRef(None)
        assert len(set.getDataTypeRefs()) == 1

        # Test literalPrefix methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        literal = ARLiteral()
        literal.setValue("test_prefix")
        set.setLiteralPrefix(literal)
        assert set.getLiteralPrefix() == literal

        # Test setLiteralPrefix with None
        set.setLiteralPrefix(None)
        assert set.getLiteralPrefix() == literal
