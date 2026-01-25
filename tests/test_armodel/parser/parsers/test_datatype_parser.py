"""Test DataTypeParser methods."""
from armodel.parser.parsers.datatype_parser import DataTypeParser
from armodel.parser.parsers.common_structure_parser import (
    CommonStructureParser,
)


class TestDataTypeParser:
    """Test DataTypeParser."""

    def test_datatype_parser_initialization(self):
        """Test that DataTypeParser can be initialized."""
        parser = DataTypeParser()
        assert parser is not None
        assert hasattr(parser, 'readAutosarDataType')
        assert hasattr(parser, 'readApplicationPrimitiveDataType')
        assert hasattr(parser, 'readCompuMethod')
        assert hasattr(parser, 'readDataConstr')
        assert hasattr(parser, 'readUnit')

    def test_datatype_parser_with_parent_parser(self):
        """Test that DataTypeParser can accept parent parser."""
        common_parser = CommonStructureParser()
        parser = DataTypeParser(parent_parser=common_parser)
        assert parser._parent_parser == common_parser

    def test_read_autosar_data_type_method_exists(self):
        """Test that readAutosarDataType method exists and is callable."""
        parser = DataTypeParser()
        assert callable(parser.readAutosarDataType)
        assert hasattr(parser.readAutosarDataType, '__self__')

    def test_all_required_methods_exist(self):
        """Test that all required DataType methods exist."""
        parser = DataTypeParser()
        required_methods = [
            'readAutosarDataType',
            'readApplicationPrimitiveDataType',
            'readApplicationRecordElement',
            'readApplicationRecordDataTypeElements',
            'readApplicationRecordDataType',
            'readImplementationDataTypeElement',
            'readImplementationDataTypeSubElements',
            'readImplementationDataType',
            'readImplementationDataTypeSymbolProps',
            'readApplicationDataType',
            'readApplicationCompositeDataType',
            'readDataPrototype',
            'readApplicationCompositeElementDataPrototype',
            'readApplicationArrayElement',
            'readApplicationArrayDataType',
            'readDataTypeMappingRefs',
            'readDataTypeMaps',
            'readModeRequestTypeMaps',
            'readDataTypeMappingSet',
            'readCompositionSwComponentTypeDataTypeMappingSet',
            'readCompuConst',
            'readCompuNominatorDenominator',
            'readCompuRationCoeffs',
            'readCompuScaleContents',
            'readCompuScale',
            'readCompuMethod',
            'readInternalConstrs',
            'readPhysConstrs',
            'readDataConstrRule',
            'readDataConstr',
            'readUnit',
            'readImplementationProps',
            'readSymbolProps',
        ]

        for method_name in required_methods:
            assert hasattr(parser, method_name), \
                f"Missing method: {method_name}"
            assert callable(getattr(parser, method_name)), \
                f"Method {method_name} is not callable"
