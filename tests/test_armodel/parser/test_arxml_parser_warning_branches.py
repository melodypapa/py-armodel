"""Tests for warning-mode fallback branches and edge cases in ARXMLParser.

Targets:
- notImplemented/raiseError sites in warning mode
- Optional getter None-return branches
- raiseWarning and try/except paths
- load() error cases and boundary conditions
"""

import logging
import os
import tempfile

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease('R23-11')
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease('R23-11')
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    """Parser configured in warning mode (logs instead of raising)."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease('R23-11')
    return ARXMLParser(options={"warning": True})


def _snip(inner_xml: str) -> ET.Element:
    """Create an XML element from inner XML string."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner_xml}</ROOT>")


# ==================== TestWarningModeFallbackBranches ====================


class TestWarningModeFallbackBranches:
    """Test that notImplemented/raiseError sites log warnings instead of raising."""

    def test_unsupported_provided_mode_group_logs_warning(self, warning_parser, caplog):
        """Test unsupported ProvidedModeGroup logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        bsw = pkg.createBswModuleDescription("Bsw")
        element = _snip("""
            <PROVIDED-MODE-GROUPS>
                <UNKNOWN-MODE-GROUP>
                    <SHORT-NAME>MG</SHORT-NAME>
                </UNKNOWN-MODE-GROUP>
            </PROVIDED-MODE-GROUPS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionProvidedModeGroups(element, bsw)
        assert any("Unsupported ProvidedModeGroup" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_required_mode_group_logs_warning(self, warning_parser, caplog):
        """Test unsupported RequiredModeGroup logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        bsw = pkg.createBswModuleDescription("Bsw")
        element = _snip("""
            <REQUIRED-MODE-GROUPS>
                <UNKNOWN-MODE-GROUP>
                    <SHORT-NAME>MG</SHORT-NAME>
                </UNKNOWN-MODE-GROUP>
            </REQUIRED-MODE-GROUPS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionRequiredModeGroups(element, bsw)
        assert any("Unsupported RequiredModeGroup" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_data_receive_point_logs_warning(self, warning_parser, caplog):
        """Test unsupported Data Element logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        iface = pkg.createSenderReceiverInterface("SRInterface")
        element = _snip("""
            <DATA-ELEMENTS>
                <UNKNOWN-POINT>
                    <SHORT-NAME>DP</SHORT-NAME>
                </UNKNOWN-POINT>
            </DATA-ELEMENTS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSenderReceiverInterfaceDataElements(element, iface)
        assert any("Unsupported Data Element" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_runnables_logs_warning(self, warning_parser, caplog):
        """Test unsupported Runnables logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        swc = pkg.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("Behavior")
        element = _snip("""
            <RUNNABLES>
                <UNKNOWN-RUNNABLE>
                    <SHORT-NAME>Run</SHORT-NAME>
                </UNKNOWN-RUNNABLE>
            </RUNNABLES>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehavior(element, behavior)
        assert any("Unsupported Runnables" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_swc_internal_behavior_event_logs_warning(self, warning_parser, caplog):
        """Test unsupported SwcInternalBehavior Event logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        swc = pkg.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("Behavior")
        element = _snip("""
            <EVENTS>
                <UNKNOWN-EVENT>
                    <SHORT-NAME>Evt</SHORT-NAME>
                </UNKNOWN-EVENT>
            </EVENTS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehavior(element, behavior)
        assert any("Unsupported SwcInternalBehavior Event" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_port_prototype_logs_warning(self, warning_parser, caplog):
        """Test unsupported Port Prototype logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        swc = pkg.createApplicationSwComponentType("Swc")
        element = _snip("""
            <PORTS>
                <UNKNOWN-PORT>
                    <SHORT-NAME>Port</SHORT-NAME>
                </UNKNOWN-PORT>
            </PORTS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwComponentTypePorts(element, swc)
        assert any("Unsupported Port Prototype" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_operation_logs_warning(self, warning_parser, caplog):
        """Test unsupported Operation logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        iface = pkg.createClientServerInterface("CSInterface")
        element = _snip("""
            <OPERATIONS>
                <UNKNOWN-OPERATION>
                    <SHORT-NAME>Op</SHORT-NAME>
                </UNKNOWN-OPERATION>
            </OPERATIONS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readClientServerInterface(element, iface)
        assert any("Unsupported Operation" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_parameter_logs_warning(self, warning_parser, caplog):
        """Test unsupported Parameter logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        iface = pkg.createParameterInterface("ParamInterface")
        element = _snip("""
            <PARAMETERS>
                <UNKNOWN-PARAMETER>
                    <SHORT-NAME>Param</SHORT-NAME>
                </UNKNOWN-PARAMETER>
            </PARAMETERS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readParameterInterface(element, iface)
        assert any("Unsupported Parameter" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_nvdata_logs_warning(self, warning_parser, caplog):
        """Test unsupported NvData logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        iface = pkg.createNvDataInterface("NVInterface")
        element = _snip("""
            <NV-DATAS>
                <UNKNOWN-NV-DATA>
                    <SHORT-NAME>NV</SHORT-NAME>
                </UNKNOWN-NV-DATA>
            </NV-DATAS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readNvDataInterface(element, iface)
        assert any("Unsupported NvData" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_application_record_element_logs_warning(self, warning_parser, caplog):
        """Test unsupported ApplicationRecordDataType Element logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        data_type = pkg.createApplicationRecordDataType("RecordType")
        element = _snip("""
            <ELEMENTS>
                <UNKNOWN-ELEMENT>
                    <SHORT-NAME>Elem</SHORT-NAME>
                </UNKNOWN-ELEMENT>
            </ELEMENTS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readApplicationRecordDataTypeElements(element, data_type)
        assert any("Unsupported ApplicationRecordDataType Element" in rec.getMessage() for rec in caplog.records)

    def test_unsupported_implementation_data_type_subelement_logs_warning(self, warning_parser, caplog):
        """Test unsupported ImplementationDataType SubElement logs warning."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        data_type = pkg.createImplementationDataType("ImplType")
        element = _snip("""
            <SUB-ELEMENTS>
                <UNKNOWN-SUB-ELEMENT>
                    <SHORT-NAME>Sub</SHORT-NAME>
                </UNKNOWN-SUB-ELEMENT>
            </SUB-ELEMENTS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readImplementationDataTypeSubElements(element, data_type)
        assert any("Unsupported ImplementationDataType SubElement" in rec.getMessage() for rec in caplog.records)


class TestRaiseErrorWarningMode:
    """Test raiseError sites in warning mode."""

    def test_raise_error_invalid_arxml_file_logs_warning(self, warning_parser, caplog):
        """Test invalid ARXML file logs warning instead of raising."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write("<?xml version='1.0'?>\n<NOT-AUTOSAR></NOT-AUTOSAR>")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            with caplog.at_level(logging.ERROR):
                warning_parser.load(temp_path, AUTOSAR.getInstance())
            assert any("Invalid ARXML file" in rec.getMessage() for rec in caplog.records)
        finally:
            os.unlink(temp_path)


# ==================== TestOptionalGetterDefensivePaths ====================


class TestOptionalGetterDefensivePaths:
    """Test None-return branches of optional getter methods."""

    def test_getChildElementOptionalRefType_missing_returns_None(self, parser):
        """Test getChildElementOptionalRefType returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        assert parser.getChildElementOptionalRefType(element, "MISSING-REF") is None

    def test_getChildElementOptionalRefType_with_base_and_dest(self, parser):
        """Test getChildElementOptionalRefType with BASE and DEST attributes."""
        element = _snip('<R BASE="b" DEST="UNIT">/pkg/u</R>')
        ref = parser.getChildElementOptionalRefType(element, "R")
        assert ref is not None
        assert ref.getBase() == "b"
        assert ref.getDest() == "UNIT"
        assert ref.getValue() == "/pkg/u"

    def test_getSwPointerTargetProps_missing_returns_None(self, parser):
        """Test getSwPointerTargetProps returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getSwPointerTargetProps(element, "SW-POINTER-TARGET-PROPS")
        assert result is None

    def test_getSwPointerTargetProps_present_returns_props(self, parser):
        """Test getSwPointerTargetProps returns props when element present."""
        element = _snip("""
            <SW-POINTER-TARGET-PROPS>
                <TARGET-CATEGORY>DATA</TARGET-CATEGORY>
            </SW-POINTER-TARGET-PROPS>
        """)
        result = parser.getSwPointerTargetProps(element, "SW-POINTER-TARGET-PROPS")
        assert result is not None
        assert result.targetCategory is not None

    def test_getSwDataDefProps_missing_returns_None(self, parser):
        """Test getSwDataDefProps returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        assert result is None

    def test_getSwDataDefProps_no_conditional_returns_None(self, parser):
        """Test getSwDataDefProps returns None when conditional missing."""
        element = _snip("""
            <SW-DATA-DEF-PROPS>
                <SW-DATA-DEF-PROPS-VARIANTS>
                </SW-DATA-DEF-PROPS-VARIANTS>
            </SW-DATA-DEF-PROPS>
        """)
        result = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        assert result is None

    def test_getSwDataDefProps_present_returns_props(self, parser):
        """Test getSwDataDefProps returns props when properly formed."""
        element = _snip("""
            <SW-DATA-DEF-PROPS>
                <SW-DATA-DEF-PROPS-VARIANTS>
                    <SW-DATA-DEF-PROPS-CONDITIONAL>
                        <BASE-TYPE-REF>/BaseType</BASE-TYPE-REF>
                    </SW-DATA-DEF-PROPS-CONDITIONAL>
                </SW-DATA-DEF-PROPS-VARIANTS>
            </SW-DATA-DEF-PROPS>
        """)
        result = parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        assert result is not None
        assert result.baseTypeRef is not None

    def test_getVariableInAtomicSWCTypeInstanceRef_none_element(self, parser):
        """Test getVariableInAtomicSWCTypeInstanceRef with None element."""
        result = parser.getVariableInAtomicSWCTypeInstanceRef(None)
        assert result is None

    def test_getVariableInAtomicSWCTypeInstanceRef_present(self, parser):
        """Test getVariableInAtomicSWCTypeInstanceRef with element."""
        element = _snip("""
            <AUTOSAR-VARIABLE-IREF>
                <PORT-PROTOTYPE-REF>/Port</PORT-PROTOTYPE-REF>
                <TARGET-DATA-PROTOTYPE-REF>/Data</TARGET-DATA-PROTOTYPE-REF>
            </AUTOSAR-VARIABLE-IREF>
        """)
        result = parser.getVariableInAtomicSWCTypeInstanceRef(element)
        assert result is not None

    def test_getComponentInSystemInstanceRef_none_element(self, parser):
        """Test getComponentInSystemInstanceRef with None element."""
        result = parser.getComponentInSystemInstanceRef(None)
        assert result is None

    def test_getComponentInSystemInstanceRef_present(self, parser):
        """Test getComponentInSystemInstanceRef with element."""
        element = _snip("""
            <COMPONENT-IREF>
                <BASE-REF>/Base</BASE-REF>
                <TARGET-COMPONENT-REF>/Target</TARGET-COMPONENT-REF>
            </COMPONENT-IREF>
        """)
        result = parser.getComponentInSystemInstanceRef(element)
        assert result is not None

    def test_getAutosarVariableRef_missing_returns_None(self, parser):
        """Test getAutosarVariableRef returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")
        assert result is None

    def test_getAutosarVariableRef_present(self, parser):
        """Test getAutosarVariableRef with element."""
        element = _snip("""
            <ACCESSED-VARIABLE>
                <AUTOSAR-VARIABLE-IREF>
                    <PORT-PROTOTYPE-REF>/Port</PORT-PROTOTYPE-REF>
                    <TARGET-DATA-PROTOTYPE-REF>/Data</TARGET-DATA-PROTOTYPE-REF>
                </AUTOSAR-VARIABLE-IREF>
            </ACCESSED-VARIABLE>
        """)
        result = parser.getAutosarVariableRef(element, "ACCESSED-VARIABLE")
        assert result is not None

    def test_getMultiLanguageParagraphs_empty_returns_empty_list(self, parser):
        """Test getMultiLanguageParagraphs returns empty list for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getMultiLanguageParagraphs(element, "P")
        assert result == []

    def test_getMultiLanguageParagraphs_present(self, parser):
        """Test getMultiLanguageParagraphs with elements."""
        element = _snip("""
            <P>
                <L-1 L="EN">Text</L-1>
            </P>
        """)
        result = parser.getMultiLanguageParagraphs(element, "P")
        assert len(result) == 1

    def test_getLParagraphs_empty_returns_empty_list(self, parser):
        """Test getLParagraphs returns empty list for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getLParagraphs(element, "L-1")
        assert result == []

    def test_getLParagraphs_present(self, parser):
        """Test getLParagraphs with elements."""
        element = _snip("""
            <CONTAINER>
                <L-1 L="EN">Text</L-1>
                <L-1 L="DE">Text</L-1>
            </CONTAINER>
        """)
        result = parser.getLParagraphs(element, "CONTAINER/L-1")
        assert len(result) == 2

    def test_getSwValues_missing_returns_None(self, parser):
        """Test getSwValues returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getSwValues(element, "SW-VALUES")
        assert result is None

    def test_getSwValues_present(self, parser):
        """Test getSwValues with element."""
        element = _snip("""
            <SW-VALUES>
                <V>1.0</V>
                <V>2.0</V>
            </SW-VALUES>
        """)
        result = parser.getSwValues(element, "SW-VALUES")
        assert result is not None

    def test_getValueList_missing_returns_None(self, parser):
        """Test getValueList returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getValueList(element, "VALUE-LIST")
        assert result is None

    def test_getValueList_present(self, parser):
        """Test getValueList with element."""
        element = _snip("""
            <VALUE-LIST>
                <V>1.0</V>
            </VALUE-LIST>
        """)
        result = parser.getValueList(element, "VALUE-LIST")
        assert result is not None

    def test_getApplicationCompositeElementInPortInterfaceInstanceRef_missing(self, parser):
        """Test getApplicationCompositeElementInPortInterfaceInstanceRef returns None."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")
        assert result is None

    def test_getApplicationCompositeElementInPortInterfaceInstanceRef_present(self, parser):
        """Test getApplicationCompositeElementInPortInterfaceInstanceRef with element."""
        element = _snip("""
            <LEAF-ELEMENT-IREF>
                <ROOT-DATA-PROTOTYPE-REF>/Root</ROOT-DATA-PROTOTYPE-REF>
                <TARGET-DATA-PROTOTYPE-REF>/Target</TARGET-DATA-PROTOTYPE-REF>
            </LEAF-ELEMENT-IREF>
        """)
        result = parser.getApplicationCompositeElementInPortInterfaceInstanceRef(element, "LEAF-ELEMENT-IREF")
        assert result is not None

    def test_getGraphic_missing_returns_None(self, parser):
        """Test getGraphic returns None for missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getGraphic(element, "GRAPHIC")
        assert result is None

    def test_getGraphic_present(self, parser):
        """Test getGraphic with element."""
        element = _snip('<GRAPHIC FILENAME="test.png"/>')
        result = parser.getGraphic(element, "GRAPHIC")
        assert result is not None
        assert result.filename == "test.png"


# ==================== TestRaiseWarningFallbacks ====================


class TestRaiseWarningFallbacks:
    """Test raiseWarning and try/except paths."""

    def test_raiseWarning_always_logs(self, parser, caplog):
        """Test raiseWarning always logs regardless of warning mode."""
        with caplog.at_level(logging.WARNING):
            parser.raiseWarning("test warning message")
        assert any("test warning message" in rec.getMessage() for rec in caplog.records)

    def test_raiseWarning_in_warning_mode(self, warning_parser, caplog):
        """Test raiseWarning works in warning mode."""
        with caplog.at_level(logging.WARNING):
            warning_parser.raiseWarning("warning mode test")
        assert any("warning mode test" in rec.getMessage() for rec in caplog.records)

    def test_notImplemented_warning_mode_logs_error(self, warning_parser, caplog):
        """Test notImplemented logs error in warning mode."""
        with caplog.at_level(logging.ERROR):
            warning_parser.notImplemented("Unsupported element type")
        assert any("Unsupported element type" in rec.getMessage() for rec in caplog.records)

    def test_notImplemented_raise_mode_raises(self, parser):
        """Test notImplemented raises in raise mode."""
        with pytest.raises(NotImplementedError, match="Unsupported element"):
            parser.notImplemented("Unsupported element")

    def test_raiseError_warning_mode_logs_error(self, warning_parser, caplog):
        """Test raiseError logs error in warning mode."""
        with caplog.at_level(logging.ERROR):
            warning_parser.raiseError("Error message in warning mode")
        assert any("Error message in warning mode" in rec.getMessage() for rec in caplog.records)

    def test_raiseError_raise_mode_raises(self, parser):
        """Test raiseError raises in raise mode."""
        with pytest.raises(ValueError, match="Error message"):
            parser.raiseError("Error message")

    def test_warning_mode_multiple_notImplemented_calls(self, warning_parser, caplog):
        """Test multiple notImplemented calls in warning mode."""
        with caplog.at_level(logging.ERROR):
            warning_parser.notImplemented("First unsupported")
            warning_parser.notImplemented("Second unsupported")
            warning_parser.notImplemented("Third unsupported")
        error_messages = [rec.getMessage() for rec in caplog.records]
        assert "First unsupported" in error_messages[0]
        assert "Second unsupported" in error_messages[1]
        assert "Third unsupported" in error_messages[2]

    def test_warning_mode_mixed_errors_and_warnings(self, warning_parser, caplog):
        """Test mixed raiseError and raiseWarning calls."""
        with caplog.at_level(logging.WARNING):
            warning_parser.raiseError("An error occurred")
            warning_parser.raiseWarning("A warning occurred")

        assert any("An error occurred" in rec.getMessage() for rec in caplog.records if rec.levelno == logging.ERROR)
        assert any("A warning occurred" in rec.getMessage() for rec in caplog.records if rec.levelno == logging.WARNING)

    def test_readRootSwCompositionPrototype_value_error_to_warning(self, warning_parser, caplog):
        """Test readRootSwCompositionPrototype ValueError→raiseWarning path."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        pkg = doc.createARPackage("Pkg")
        system = pkg.createSystem("System")

        element = _snip("""
            <ROOT-SOFTWARE-COMPOSITIONS>
                <ROOT-SW-COMPOSITION-PROTOTYPE>
                    <SHORT-NAME>Root1</SHORT-NAME>
                </ROOT-SW-COMPOSITION-PROTOTYPE>
            </ROOT-SOFTWARE-COMPOSITIONS>
        """)

        with caplog.at_level(logging.WARNING):
            warning_parser.readRootSwCompositionPrototype(element, system)


# ==================== TestLoadAndDispatchBoundaries ====================


class TestLoadAndDispatchBoundaries:
    """Test load() error cases and boundary conditions."""

    def test_load_invalid_arxml_raises_in_raise_mode(self, parser):
        """Test load() raises on invalid ARXML in raise mode."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write("<?xml version='1.0'?>\n<NOT-AUTOSAR></NOT-AUTOSAR>")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            with pytest.raises(ValueError, match="Invalid ARXML file"):
                parser.load(temp_path, AUTOSAR.getInstance())
        finally:
            os.unlink(temp_path)

    def test_load_valid_minimal_arxml(self, parser):
        """Test load() with valid minimal ARXML document."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write(f"""<?xml version='1.0'?>
<AUTOSAR xmlns='{NS}'>
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>TestPkg</SHORT-NAME>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>""")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            document = AUTOSAR.getInstance()
            parser.load(temp_path, document)
            pkgs = document.getARPackages()
            assert len(pkgs) > 0
            found = False
            for pkg in pkgs:
                if pkg.getShortName() == "TestPkg":
                    found = True
                    break
            assert found
        finally:
            os.unlink(temp_path)

    def test_load_empty_ar_packages(self, parser):
        """Test load() with empty AR-PACKAGES element."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write(f"""<?xml version='1.0'?>
<AUTOSAR xmlns='{NS}'>
    <AR-PACKAGES>
    </AR-PACKAGES>
</AUTOSAR>""")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            document = AUTOSAR.getInstance()
            parser.load(temp_path, document)
        finally:
            os.unlink(temp_path)

    def test_load_no_ar_packages(self, parser):
        """Test load() with no AR-PACKAGES element."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write(f"""<?xml version='1.0'?>
<AUTOSAR xmlns='{NS}'>
</AUTOSAR>""")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            document = AUTOSAR.getInstance()
            parser.load(temp_path, document)
        finally:
            os.unlink(temp_path)

    def test_load_with_reference_bases(self, parser):
        """Test load() with REFERENCE-BASES element."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write(f"""<?xml version='1.0'?>
<AUTOSAR xmlns='{NS}'>
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>TestPkg</SHORT-NAME>
            <REFERENCE-BASES>
                <REFERENCE-BASE>
                    <SHORT-LABEL>BaseLabel</SHORT-LABEL>
                    <IS-DEFAULT>true</IS-DEFAULT>
                </REFERENCE-BASE>
            </REFERENCE-BASES>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>""")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            document = AUTOSAR.getInstance()
            parser.load(temp_path, document)
            pkgs = document.getARPackages()
            assert len(pkgs) > 0
        finally:
            os.unlink(temp_path)

    def test_load_with_admin_data(self, parser):
        """Test load() with ADMIN-DATA element."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.arxml', delete=False) as f:
            f.write(f"""<?xml version='1.0'?>
<AUTOSAR xmlns='{NS}'>
    <ADMIN-DATA>
        <DOC-REVISIONS>
            <DOC-REVISION>
                <ISSUE>1.0</ISSUE>
            </DOC-REVISION>
        </DOC-REVISIONS>
    </ADMIN-DATA>
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>TestPkg</SHORT-NAME>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>""")
            f.flush()
            temp_path = f.name

        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease('R23-11')
            document = AUTOSAR.getInstance()
            parser.load(temp_path, document)
            assert document.adminData is not None
        finally:
            os.unlink(temp_path)

    def test_readARPackages_empty_packages(self, parser):
        """Test readARPackages with no packages."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        document = AUTOSAR.getInstance()
        element = ET.fromstring(f"<AUTOSAR xmlns='{NS}'></AUTOSAR>")
        parser.readARPackages(element, document)

    def test_readARPackage_orchestrator(self, parser):
        """Test readARPackage orchestrator method."""
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease('R23-11')
        doc = AUTOSAR.getInstance()
        parent_pkg = doc.createARPackage("Parent")

        element = _snip("""
            <AR-PACKAGE>
                <SHORT-NAME>Child</SHORT-NAME>
            </AR-PACKAGE>
        """)

        child_pkg = parent_pkg.createARPackage("Child")
        parser.readARPackage(element, child_pkg)


# ==================== Additional Error Branch Tests ====================


class TestAdditionalErrorBranches:
    """Additional tests for error/warning branches."""

    def test_getTagName_with_element(self, parser):
        """Test getTagName with ET.Element."""
        element = _snip("<TEST/>")
        assert parser.getTagName(element) == "ROOT"

    def test_getTagName_with_string(self, parser):
        """Test getTagName with string tag."""
        assert parser.getTagName(f"{{{NS}}}TEST") == "TEST"
        assert parser.getTagName("PLAIN-TAG") == "PLAIN-TAG"

    def test_getTagName_invalid_type_raises(self, parser):
        """Test getTagName with invalid type raises error."""
        with pytest.raises(ValueError, match="Invalid Tag type"):
            parser.getTagName(123)

    def test_getTagName_invalid_type_warning_mode(self, warning_parser, caplog):
        """Test getTagName with invalid type logs error in warning mode."""
        with caplog.at_level(logging.ERROR):
            warning_parser.getTagName(123)
        assert any("Invalid Tag type" in rec.getMessage() for rec in caplog.records)

    def test_find_with_wildcard(self, parser):
        """Test find method with wildcard."""
        element = _snip("""
            <CONTAINER>
                <CHILD>Value</CHILD>
            </CONTAINER>
        """)
        child = parser.find(element, "CONTAINER/*")
        assert child is not None

    def test_findall_empty_result(self, parser):
        """Test findall returns empty list for missing elements."""
        element = _snip("<CONTAINER/>")
        result = parser.findall(element, "NON-EXISTENT/*")
        assert result == []

    def test_findall_multiple_elements(self, parser):
        """Test findall returns multiple elements."""
        element = _snip("""
            <CONTAINER>
                <ITEM>1</ITEM>
                <ITEM>2</ITEM>
                <ITEM>3</ITEM>
            </CONTAINER>
        """)
        result = parser.findall(element, "CONTAINER/ITEM")
        assert len(result) == 3

    def test_getChildElementOptionalNumericalValue_missing(self, parser):
        """Test getChildElementOptionalNumericalValue with missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getChildElementOptionalNumericalValue(element, "MISSING")
        assert result is None

    def test_getChildElementOptionalNumericalValue_present(self, parser):
        """Test getChildElementOptionalNumericalValue with present element."""
        element = _snip('<NUM SHORT-LABEL="Label">42</NUM>')
        result = parser.getChildElementOptionalNumericalValue(element, "NUM")
        assert result is not None
        assert result.getValue() == 42.0

    def test_getChildElementOptionalDataTime_missing(self, parser):
        """Test getChildElementOptionalDataTime with missing element."""
        element = _snip("<SHORT-NAME>X</SHORT-NAME>")
        result = parser.getChildElementOptionalDataTime(element, "MISSING")
        assert result is None

    def test_getChildElementOptionalDataTime_present(self, parser):
        """Test getChildElementOptionalDataTime with present element."""
        element = _snip("<DT>2024-01-01T00:00:00Z</DT>")
        result = parser.getChildElementOptionalDataTime(element, "DT")
        assert result is not None