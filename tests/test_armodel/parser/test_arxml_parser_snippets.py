"""Tests for ARXML parser using authentic XML snippets.

Tests use authentic XML snippets extracted from real AUTOSAR XML files
to ensure parsing works correctly with real AUTOSAR structure patterns.
"""

import pytest
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
    AUTOSARDoc,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


# ==================== Helper Methods Tests ====================


class TestHelperMethods:
    """Test helper methods from AbstractARXMLParser."""

    def test_getTagName_with_namespace(self, parser):
        """Test getTagName with element containing namespace."""
        element = ET.fromstring(f"<SHORT-NAME xmlns='{NS}'>TestName</SHORT-NAME>")
        tag = parser.getTagName(element)
        assert tag == "SHORT-NAME"

    def test_getTagName_from_string(self, parser):
        """Test getTagName with string tag."""
        tag = parser.getTagName(f"{{{NS}}}SHORT-NAME")
        assert tag == "SHORT-NAME"

    def test_find_existing_element(self, parser):
        """Test find with existing element."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>"""
        )
        result = parser.find(element, "SHORT-NAME")
        assert result is not None
        assert result.text == "TestElement"

    def test_find_nonexistent_element(self, parser):
        """Test find with nonexistent element."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>"""
        )
        result = parser.find(element, "NONEXISTENT")
        assert result is None

    def test_find_nested_path(self, parser):
        """Test find with nested path."""
        element = ET.fromstring(
            f"""<ARGUMENT-DATA-PROTOTYPE xmlns='{NS}'>
            <SHORT-NAME>ComMode</SHORT-NAME>
            <TYPE-TREF DEST='IMPLEMENTATION-DATA-TYPE'>/DemoApplication/ImplementationDataTypes/ComM_ModeType</TYPE-TREF>
            <DIRECTION>IN</DIRECTION>
        </ARGUMENT-DATA-PROTOTYPE>"""
        )
        result = parser.find(element, "TYPE-TREF")
        assert result is not None
        assert result.get("DEST") == "IMPLEMENTATION-DATA-TYPE"

    def test_findall_multiple_elements(self, parser):
        """Test findall with multiple elements."""
        xml = f"""<PARENT xmlns='{NS}'>
            <ITEM>1</ITEM>
            <ITEM>2</ITEM>
        </PARENT>"""
        element = ET.fromstring(xml)
        results = parser.findall(element, "ITEM")
        assert len(results) == 2
        assert results[0].text == "1"
        assert results[1].text == "2"

    def test_findall_no_elements(self, parser):
        """Test findall with no matching elements."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>"""
        )
        results = parser.findall(element, "NONEXISTENT")
        assert len(results) == 0

    def test_getShortName_valid(self, parser):
        """Test getShortName with valid SHORT-NAME."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>"""
        )
        name = parser.getShortName(element)
        assert name == "TestElement"

    def test_getShortName_missing_raises_error(self, parser):
        """Test getShortName with missing SHORT-NAME raises error."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        with pytest.raises(ValueError, match="Short Name is required"):
            parser.getShortName(element)


# ==================== Element Getter Tests ====================


class TestElementGetters:
    """Test getChildElementOptional* methods."""

    def test_getChildElementOptionalLiteral_present(self, parser):
        """Test getChildElementOptionalLiteral with present element."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-LITERAL>value123</TEST-LITERAL>
        </ELEMENT>"""
        )
        result = parser.getChildElementOptionalLiteral(element, "TEST-LITERAL")
        assert result is not None
        assert result._value == "value123"

    def test_getChildElementOptionalLiteral_missing(self, parser):
        """Test getChildElementOptionalLiteral with missing element."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        result = parser.getChildElementOptionalLiteral(element, "NONEXISTENT")
        assert result is None

    def test_getChildElementOptionalLiteral_empty(self, parser):
        """Test getChildElementOptionalLiteral with empty element."""
        element = ET.fromstring(
            f"<ELEMENT xmlns='{NS}'><TEST-LITERAL></TEST-LITERAL></ELEMENT>"
        )
        result = parser.getChildElementOptionalLiteral(element, "TEST-LITERAL")
        assert result is not None
        assert result._value == ""

    def test_getChildElementOptionalRefType_with_dest(self, parser):
        """Test getChildElementOptionalRefType with DEST attribute."""
        element = ET.fromstring(
            f"""<ARGUMENT-DATA-PROTOTYPE xmlns='{NS}'>
            <SHORT-NAME>ComMode</SHORT-NAME>
            <TYPE-TREF DEST='IMPLEMENTATION-DATA-TYPE'>/DemoApplication/ImplementationDataTypes/ComM_ModeType</TYPE-TREF>
            <DIRECTION>IN</DIRECTION>
        </ARGUMENT-DATA-PROTOTYPE>"""
        )
        result = parser.getChildElementOptionalRefType(element, "TYPE-TREF")
        assert result is not None
        assert result.getDest() == "IMPLEMENTATION-DATA-TYPE"
        assert result.getValue() == "/DemoApplication/ImplementationDataTypes/ComM_ModeType"

    def test_getChildElementOptionalRefType_missing(self, parser):
        """Test getChildElementOptionalRefType with missing element."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        result = parser.getChildElementOptionalRefType(element, "NONEXISTENT")
        assert result is None

    def test_getChildElementOptionalNumericalValue_decimal(self, parser):
        """Test getChildElementOptionalNumericalValue with decimal."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <BASE-TYPE-SIZE>32</BASE-TYPE-SIZE>
        </ELEMENT>"""
        )
        result = parser.getChildElementOptionalNumericalValue(
            element, "BASE-TYPE-SIZE"
        )
        assert result is not None
        assert result._value == 32.0

    def test_getChildElementOptionalNumericalValue_negative(self, parser):
        """Test getChildElementOptionalNumericalValue with negative value."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-VALUE>-32768</TEST-VALUE>
        </ELEMENT>"""
        )
        result = parser.getChildElementOptionalNumericalValue(element, "TEST-VALUE")
        assert result is not None
        assert result._value == -32768.0

    def test_getChildElementOptionalNumericalValue_missing(self, parser):
        """Test getChildElementOptionalNumericalValue with missing element."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        result = parser.getChildElementOptionalNumericalValue(
            element, "NONEXISTENT"
        )
        assert result is None

    def test_getChildElementOptionalFloatValue(self, parser):
        """Test getChildElementOptionalFloatValue."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-VALUE>1.23e-5</TEST-VALUE>
        </ELEMENT>"""
        )
        result = parser.getChildElementOptionalFloatValue(element, "TEST-VALUE")
        assert result is not None
        assert result._value == 1.23e-05

    def test_getChildElementOptionalFloatValue_missing(self, parser):
        """Test getChildElementOptionalFloatValue with missing element."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        result = parser.getChildElementOptionalFloatValue(element, "NONEXISTENT")
        assert result is None

    def test_getChildElementOptionalBooleanValue_true(self, parser):
        """Test getChildElementOptionalBooleanValue with true."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-VALUE>true</TEST-VALUE>
        </ELEMENT>"""
        )
        result = parser.getChildElementOptionalBooleanValue(element, "TEST-VALUE")
        assert result is not None
        assert result.getValue() is True

    def test_getChildElementOptionalBooleanValue_false(self, parser):
        """Test getChildElementOptionalBooleanValue with false."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-VALUE>false</TEST-VALUE>
        </ELEMENT>"""
        )
        result = parser.getChildElementOptionalBooleanValue(element, "TEST-VALUE")
        assert result is not None
        assert result.getValue() is False

    def test_getChildElementOptionalBooleanValue_missing(self, parser):
        """Test getChildElementOptionalBooleanValue with missing element."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        result = parser.getChildElementOptionalBooleanValue(element, "NONEXISTENT")
        assert result is None

    def test_getChildElementRefTypeList(self, parser):
        """Test getChildElementRefTypeList."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-REF DEST="TYPE1">/path1</TEST-REF>
            <TEST-REF DEST="TYPE2">/path2</TEST-REF>
        </ELEMENT>"""
        )
        results = parser.getChildElementRefTypeList(element, "TEST-REF")
        assert len(results) == 2
        assert results[0].getDest() == "TYPE1"
        assert results[1].getDest() == "TYPE2"

    def test_getChildElementRefTypeList_empty(self, parser):
        """Test getChildElementRefTypeList with no elements."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        results = parser.getChildElementRefTypeList(element, "TEST-REF")
        assert len(results) == 0


# ==================== Read Methods Tests ====================


class TestReadMethods:
    """Test read* methods for common elements."""

    def test_readARObjectAttributes_with_timestamp(self, parser):
        """Test readARObjectAttributes with T attribute."""
        from armodel.models.M2.MSR.AsamHdo.AdminData import Modification

        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}' T="2023-01-01T00:00:00+08:00">
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>"""
        )
        ar_obj = Modification()
        parser.readARObjectAttributes(element, ar_obj)
        assert ar_obj.timestamp == "2023-01-01T00:00:00+08:00"

    def test_readARObjectAttributes_with_uuid(self, parser):
        """Test readARObjectAttributes with UUID attribute."""
        from armodel.models.M2.MSR.AsamHdo.AdminData import Modification

        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}' UUID="12345678-1234-1234-1234-123456789012">
            <SHORT-NAME>TestElement</SHORT-NAME>
        </ELEMENT>"""
        )
        ar_obj = Modification()
        parser.readARObjectAttributes(element, ar_obj)
        assert ar_obj.uuid == "12345678-1234-1234-1234-123456789012"

    def test_getAdminData_present(self, parser):
        """Test getAdminData with present ADMIN-DATA."""
        element = ET.fromstring(
            f"""<AUTOSAR xmlns='{NS}'>
            <ADMIN-DATA>
                <LANGUAGE>EN</LANGUAGE>
                <USED-LANGUAGES>
                    <L-10 L="EN">English</L-10>
                </USED-LANGUAGES>
            </ADMIN-DATA>
        </AUTOSAR>"""
        )
        admin_data = parser.getAdminData(element, "ADMIN-DATA")
        assert admin_data is not None
        assert admin_data.getLanguage().getValue() == "EN"

    def test_getAdminData_missing(self, parser):
        """Test getAdminData with missing ADMIN-DATA."""
        element = ET.fromstring(
            f"<AUTOSAR xmlns='{NS}'><AR-PACKAGES></AR-PACKAGES></AUTOSAR>"
        )
        admin_data = parser.getAdminData(element, "ADMIN-DATA")
        assert admin_data is None

    def test_readElementOptionalAttrib_present(self, parser):
        """Test readElementOptionalAttrib with present attribute."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}' T="2023-01-01T00:00:00">
            <SHORT-NAME>Test</SHORT-NAME>
        </ELEMENT>"""
        )
        result = parser.readElementOptionalAttrib(element, "T")
        assert result == "2023-01-01T00:00:00"

    def test_readElementOptionalAttrib_missing(self, parser):
        """Test readElementOptionalAttrib with missing attribute."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <SHORT-NAME>Test</SHORT-NAME>
        </ELEMENT>"""
        )
        result = parser.readElementOptionalAttrib(element, "T")
        assert result is None


# ==================== Reference Tests ====================


class TestReferences:
    """Test reference parsing methods."""

    def test_refType_properties(self, parser):
        """Test RefType properties from authentic snippet."""
        element = ET.fromstring(
            f"""<ARGUMENT-DATA-PROTOTYPE xmlns='{NS}'>
            <SHORT-NAME>ComMode</SHORT-NAME>
            <TYPE-TREF DEST='IMPLEMENTATION-DATA-TYPE'>/DemoApplication/ImplementationDataTypes/ComM_ModeType</TYPE-TREF>
            <DIRECTION>IN</DIRECTION>
        </ARGUMENT-DATA-PROTOTYPE>"""
        )
        ref = parser.getChildElementOptionalRefType(element, "TYPE-TREF")
        assert ref.getDest() == "IMPLEMENTATION-DATA-TYPE"
        assert ref.getValue() == "/DemoApplication/ImplementationDataTypes/ComM_ModeType"
        assert ref.getBase() is None

    def test_refType_with_base(self, parser):
        """Test RefType with BASE attribute."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <TEST-REF BASE="/base" DEST="INTERFACE">/path</TEST-REF>
        </ELEMENT>"""
        )
        ref = parser.getChildElementOptionalRefType(element, "TEST-REF")
        assert ref.getDest() == "INTERFACE"
        assert ref.getValue() == "/path"
        assert ref.getBase() == "/base"


# ==================== Limit Tests ====================


class TestLimits:
    """Test Limit parsing."""

    def test_getLimit_with_interval_type_closed(self, parser):
        """Test getChildLimitElement with INTERVAL-TYPE=CLOSED."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <LOWER-LIMIT INTERVAL-TYPE="CLOSED">-32768</LOWER-LIMIT>
        </ELEMENT>"""
        )
        limit = parser.getChildLimitElement(element, "LOWER-LIMIT")
        assert limit is not None
        assert limit.value == "-32768"
        assert limit.intervalType == "CLOSED"

    def test_getLimit_with_interval_type_open(self, parser):
        """Test getChildLimitElement with INTERVAL-TYPE=OPEN."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <LOWER-LIMIT INTERVAL-TYPE="OPEN">0</LOWER-LIMIT>
        </ELEMENT>"""
        )
        limit = parser.getChildLimitElement(element, "LOWER-LIMIT")
        assert limit is not None
        assert limit.value == "0"
        assert limit.intervalType == "OPEN"

    def test_getLimit_without_interval_type(self, parser):
        """Test getChildLimitElement without INTERVAL-TYPE."""
        element = ET.fromstring(
            f"""<ELEMENT xmlns='{NS}'>
            <LOWER-LIMIT>0</LOWER-LIMIT>
        </ELEMENT>"""
        )
        limit = parser.getChildLimitElement(element, "LOWER-LIMIT")
        assert limit is not None
        assert limit.value == "0"
        assert limit.intervalType is None

    def test_getLimit_missing(self, parser):
        """Test getChildLimitElement with missing element."""
        element = ET.fromstring(f"<ELEMENT xmlns='{NS}'/>")
        limit = parser.getChildLimitElement(element, "LOWER-LIMIT")
        assert limit is None


# ==================== ARPackage Tests ====================


class TestARPackage:
    """Test ARPackage parsing."""

    def test_readARPackages_single_package(self, parser):
        """Test readARPackages with single package."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>TestPackage</SHORT-NAME>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)
        assert len(document.getARPackages()) == 1
        assert document.getARPackages()[0].getShortName() == "TestPackage"

    def test_readARPackages_multiple_packages(self, parser):
        """Test readARPackages with multiple packages."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Package1</SHORT-NAME>
                </AR-PACKAGE>
                <AR-PACKAGE>
                    <SHORT-NAME>Package2</SHORT-NAME>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)
        assert len(document.getARPackages()) == 2
        assert document.getARPackages()[0].getShortName() == "Package1"
        assert document.getARPackages()[1].getShortName() == "Package2"

    def test_readARPackages_with_elements(self, parser):
        """Test readARPackages with packages containing elements."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>TestPackage</SHORT-NAME>
                    <ELEMENTS>
                        <IMPLEMENTATION-DATA-TYPE>
                            <SHORT-NAME>MyDataType</SHORT-NAME>
                        </IMPLEMENTATION-DATA-TYPE>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)
        assert len(document.getARPackages()) == 1


class TestSwSystemconstParser:
    """Test SwSystemconst parsing from ARXML."""

    def test_read_sw_systemconst_basic(self, parser):
        """Test parsing basic SW-SYSTEMCONST element."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Constants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>MySystemConstant</SHORT-NAME>
                        </SW-SYSTEMCONST>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        assert len(document.getARPackages()) == 1
        ar_package = document.getARPackages()[0]
        assert ar_package.getShortName() == "Constants"

        system_consts = ar_package.getSwSystemConsts()
        assert len(system_consts) == 1
        system_const = system_consts[0]
        assert system_const.getShortName() == "MySystemConstant"
        assert system_const.getSwDataDefProps() is None

    def test_read_sw_systemconst_with_sw_data_def_props(self, parser):
        """Test parsing SW-SYSTEMCONST with SW-DATA-DEF-PROPS."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Constants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>MaxValue</SHORT-NAME>
                            <SW-DATA-DEF-PROPS>
                                <SW-DATA-DEF-PROPS-VARIANTS>
                                    <SW-DATA-DEF-PROPS-CONDITIONAL>
                                        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/BaseTypes/uint32</BASE-TYPE-REF>
                                    </SW-DATA-DEF-PROPS-CONDITIONAL>
                                </SW-DATA-DEF-PROPS-VARIANTS>
                            </SW-DATA-DEF-PROPS>
                        </SW-SYSTEMCONST>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        assert len(document.getARPackages()) == 1
        ar_package = document.getARPackages()[0]
        system_const = ar_package.getSwSystemConsts()[0]
        assert system_const.getShortName() == "MaxValue"

        # Verify SW-DATA-DEF-PROPS was parsed
        assert system_const.getSwDataDefProps() is not None
        sw_data_def_props = system_const.getSwDataDefProps()
        assert sw_data_def_props.getBaseTypeRef() is not None
        assert sw_data_def_props.getBaseTypeRef().getValue() == "/BaseTypes/uint32"
        assert sw_data_def_props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"

    def test_read_sw_systemconst_multiple(self, parser):
        """Test parsing multiple SW-SYSTEMCONST elements."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Constants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>Constant1</SHORT-NAME>
                        </SW-SYSTEMCONST>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>Constant2</SHORT-NAME>
                        </SW-SYSTEMCONST>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>Constant3</SHORT-NAME>
                        </SW-SYSTEMCONST>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        system_consts = ar_package.getSwSystemConsts()
        assert len(system_consts) == 3
        assert system_consts[0].getShortName() == "Constant1"
        assert system_consts[1].getShortName() == "Constant2"
        assert system_consts[2].getShortName() == "Constant3"

    def test_read_sw_systemconst_with_category_and_admin_data(self, parser):
        """Test parsing SW-SYSTEMCONST with category and admin data."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Constants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>ConfigValue</SHORT-NAME>
                            <CATEGORY>CONSTANT</CATEGORY>
                            <ADMIN-DATA>
                                <DOCUMENTATION>
                                    <DOCUMENTATION-CLASS>SPECIFICATION</DOCUMENTATION-CLASS>
                                </DOCUMENTATION>
                            </ADMIN-DATA>
                        </SW-SYSTEMCONST>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        system_const = ar_package.getSwSystemConsts()[0]
        assert system_const.getShortName() == "ConfigValue"
        assert system_const.getCategory() is not None
        assert str(system_const.getCategory()) == "CONSTANT"

    def test_read_sw_systemconst_with_compu_method_ref(self, parser):
        """Test parsing SW-SYSTEMCONST with computation method reference."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Constants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>EncodedValue</SHORT-NAME>
                            <SW-DATA-DEF-PROPS>
                                <SW-DATA-DEF-PROPS-VARIANTS>
                                    <SW-DATA-DEF-PROPS-CONDITIONAL>
                                        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/BaseTypes/uint8</BASE-TYPE-REF>
                                        <COMPU-METHOD-REF DEST="COMPU-METHOD">/Application/CompuMethods/StatusEncoding</COMPU-METHOD-REF>
                                    </SW-DATA-DEF-PROPS-CONDITIONAL>
                                </SW-DATA-DEF-PROPS-VARIANTS>
                            </SW-DATA-DEF-PROPS>
                        </SW-SYSTEMCONST>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        system_const = ar_package.getSwSystemConsts()[0]
        assert system_const.getShortName() == "EncodedValue"
        
        sw_data_def_props = system_const.getSwDataDefProps()
        assert sw_data_def_props is not None
        assert sw_data_def_props.getCompuMethodRef() is not None
        assert sw_data_def_props.getCompuMethodRef().getValue() == "/Application/CompuMethods/StatusEncoding"

    def test_read_sw_systemconst_empty_sw_data_def_props(self, parser):
        """Test parsing SW-SYSTEMCONST with empty SW-DATA-DEF-PROPS."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Constants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONST>
                            <SHORT-NAME>SimpleValue</SHORT-NAME>
                            <SW-DATA-DEF-PROPS>
                                <SW-DATA-DEF-PROPS-VARIANTS>
                                    <SW-DATA-DEF-PROPS-CONDITIONAL>
                                    </SW-DATA-DEF-PROPS-CONDITIONAL>
                                </SW-DATA-DEF-PROPS-VARIANTS>
                            </SW-DATA-DEF-PROPS>
                        </SW-SYSTEMCONST>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""
        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        system_const = ar_package.getSwSystemConsts()[0]
        assert system_const.getShortName() == "SimpleValue"
        
        sw_data_def_props = system_const.getSwDataDefProps()
        assert sw_data_def_props is not None
        assert sw_data_def_props.getBaseTypeRef() is None
        assert sw_data_def_props.getCompuMethodRef() is None


class TestSwSystemconstantValueSetParser:
    """Test SwSystemconstantValueSet parsing from ARXML."""

    def test_read_sw_systemconstant_value_set_basic(self, parser):
        """Test parsing SW-SYSTEMCONSTANT-VALUE-SET with one value."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Variants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONSTANT-VALUE-SET>
                            <SHORT-NAME>MyValueSet</SHORT-NAME>
                            <SW-SYSTEMCONSTANT-VALUES>
                                <SW-SYSTEMCONST-VALUE>
                                    <SW-SYSTEMCONST-REF DEST="SW-SYSTEMCONST">/Constants/MySystemConstant</SW-SYSTEMCONST-REF>
                                    <VALUE>42</VALUE>
                                </SW-SYSTEMCONST-VALUE>
                            </SW-SYSTEMCONSTANT-VALUES>
                        </SW-SYSTEMCONSTANT-VALUE-SET>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""

        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        ar_package = document.getARPackages()[0]
        value_sets = ar_package.getSwSystemconstantValueSets()
        assert len(value_sets) == 1

        value_set = value_sets[0]
        assert value_set.getShortName() == "MyValueSet"
        values = value_set.getSwSystemconstantValues()
        assert len(values) == 1

        value = values[0]
        assert value.getSwSystemconstRef() is not None
        assert value.getSwSystemconstRef().getValue() == "/Constants/MySystemConstant"
        assert value.getSwSystemconstRef().getDest() == "SW-SYSTEMCONST"
        assert value.getSwSystemconst() is not None
        assert value.getValue() is not None
        assert value.getValue().getValue() == 42

    def test_read_sw_systemconstant_value_set_with_annotation(self, parser):
        """Test parsing SW-SYSTEMCONST-VALUE annotations."""
        xml = f"""<AUTOSAR xmlns='{NS}'>
            <AR-PACKAGES>
                <AR-PACKAGE>
                    <SHORT-NAME>Variants</SHORT-NAME>
                    <ELEMENTS>
                        <SW-SYSTEMCONSTANT-VALUE-SET>
                            <SHORT-NAME>AnnotatedValueSet</SHORT-NAME>
                            <SW-SYSTEMCONSTANT-VALUES>
                                <SW-SYSTEMCONST-VALUE>
                                    <ANNOTATIONS>
                                        <ANNOTATION>
                                            <ANNOTATION-ORIGIN>TEST</ANNOTATION-ORIGIN>
                                        </ANNOTATION>
                                    </ANNOTATIONS>
                                    <SW-SYSTEMCONST-REF DEST="SW-SYSTEMCONST">/Constants/Cfg</SW-SYSTEMCONST-REF>
                                    <VALUE>7</VALUE>
                                </SW-SYSTEMCONST-VALUE>
                            </SW-SYSTEMCONSTANT-VALUES>
                        </SW-SYSTEMCONSTANT-VALUE-SET>
                    </ELEMENTS>
                </AR-PACKAGE>
            </AR-PACKAGES>
        </AUTOSAR>"""

        element = ET.fromstring(xml)
        document = AUTOSARDoc()
        parser.readARPackages(element, document)

        value_set = document.getARPackages()[0].getSwSystemconstantValueSets()[0]
        value = value_set.getSwSystemconstantValues()[0]
        annotations = value.getAnnotations()
        assert len(annotations) == 1
        assert annotations[0].getAnnotationOrigin().getValue() == "TEST"