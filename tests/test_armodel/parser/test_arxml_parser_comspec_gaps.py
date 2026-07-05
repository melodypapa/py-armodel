"""Tests for ComSpec handler gaps."""
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock
import pytest
from armodel.models import AUTOSAR
from armodel.models import ApplicationSwComponentType
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


def _make_r_port():
    app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
    return app.createRPortPrototype("RPort")


def _make_p_port():
    app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
    return app.createPPortPrototype("PPort")


class TestGetClientComSpec:
    """Tests for getClientComSpec (L2005-2009)."""

    def test_with_operation_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/if/Op</OPERATION-REF>',
            root_tag="CLIENT-COM-SPEC",
        )
        result = parser.getClientComSpec(element)
        assert result is not None
        assert result.getOperationRef() is not None
        assert result.getOperationRef().getValue() == "/if/Op"
        assert result.getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

    def test_without_operation_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="CLIENT-COM-SPEC")
        result = parser.getClientComSpec(element)
        assert result is not None
        assert result.getOperationRef() is None


class TestGetParameterRequireComSpec:
    """Tests for getParameterRequireComSpec (L2011-2016)."""

    def test_with_parameter_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/pdp/Param</PARAMETER-REF>',
            root_tag="PARAMETER-REQUIRE-COM-SPEC",
        )
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert result.getParameterRef() is not None
        assert result.getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        assert result.getParameterRef().getValue() == "/pdp/Param"

    def test_without_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="PARAMETER-REQUIRE-COM-SPEC")
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert result.getParameterRef() is None
        assert result.getInitValue() is None


class TestGetQueuedReceiverComSpec:
    """Tests for getQueuedReceiverComSpec (L2025-2030)."""

    def test_with_queue_length(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            "<QUEUE-LENGTH>10</QUEUE-LENGTH>",
            root_tag="QUEUED-RECEIVER-COM-SPEC",
        )
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert result.getQueueLength() is not None
        assert result.getQueueLength().getValue() == 10.0

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="QUEUED-RECEIVER-COM-SPEC")
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert result.getQueueLength() is None


class TestGetModeSwitchReceiverComSpec:
    """Tests for getModeSwitchReceiverComSpec (L2032-2038)."""

    def test_with_all_fields(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <ENHANCED-MODE-API>true</ENHANCED-MODE-API>
            <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
            <SUPPORTS-ASYNCHRONOUS-MODE-SWITCH>false</SUPPORTS-ASYNCHRONOUS-MODE-SWITCH>
            """,
            root_tag="MODE-SWITCH-RECEIVER-COM-SPEC",
        )
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is not None
        assert result.getModeGroupRef() is not None
        assert result.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert result.getSupportsAsynchronousModeSwitch() is not None

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="MODE-SWITCH-RECEIVER-COM-SPEC")
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is None
        assert result.getModeGroupRef() is None
        assert result.getSupportsAsynchronousModeSwitch() is None


class TestGetNonqueuedReceiverComSpec:
    """Tests for getNonqueuedReceiverComSpec (L2040-2050)."""

    def test_with_data_element_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Elem</DATA-ELEMENT-REF>
            <ALIVE-TIMEOUT>0.5</ALIVE-TIMEOUT>
            <ENABLE-UPDATE>true</ENABLE-UPDATE>
            <HANDLE-NEVER-RECEIVED>false</HANDLE-NEVER-RECEIVED>
            <HANDLE-TIMEOUT-TYPE>REPLACE</HANDLE-TIMEOUT-TYPE>
            """,
            root_tag="NONQUEUED-RECEIVER-COM-SPEC",
        )
        result = parser.getNonqueuedReceiverComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is not None
        assert result.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert result.getAliveTimeout() is not None
        assert result.getEnableUpdated() is not None
        assert result.getHandleNeverReceived() is not None
        assert result.getHandleTimeoutType() is not None

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="NONQUEUED-RECEIVER-COM-SPEC")
        result = parser.getNonqueuedReceiverComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is None
        assert result.getAliveTimeout() is None
        assert result.getFilter() is None
        assert result.getInitValue() is None


class TestReadRequiredComSpec:
    """Tests for readRequiredComSpec (L2052-2068)."""

    @pytest.mark.parametrize("tag", [
        "MODE-SWITCH-RECEIVER-COM-SPEC",
        "PARAMETER-REQUIRE-COM-SPEC",
    ])
    def test_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip(
            f"""
            <REQUIRED-COM-SPECS>
                <{tag}></{tag}>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, r_port)
        specs = r_port.getRequiredComSpecs()
        assert len(specs) == 1

    def test_nv_require_branch_with_mock_parent(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        mock_parent = MagicMock()
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <NV-REQUIRE-COM-SPEC></NV-REQUIRE-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, mock_parent)
        assert mock_parent.addRequiredComSpec.called
        com_spec = mock_parent.addRequiredComSpec.call_args[0][0]
        assert com_spec is not None

    def test_unknown_branch_raises(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        with pytest.raises(ValueError):
            parser.readRequiredComSpec(element, r_port)

    def test_unknown_branch_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        warning_parser.readRequiredComSpec(element, r_port)
        assert len(r_port.getRequiredComSpecs()) == 0

    def test_empty_required_com_specs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip("")
        parser.readRequiredComSpec(element, r_port)
        assert len(r_port.getRequiredComSpecs()) == 0


class TestGetQueuedSenderComSpec:
    """Tests for getQueuedSenderComSpec (L2162-2165)."""

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="QUEUED-SENDER-COM-SPEC")
        result = parser.getQueuedSenderComSpec(element)
        assert result is not None

    def test_with_data_element_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Elem</DATA-ELEMENT-REF>',
            root_tag="QUEUED-SENDER-COM-SPEC",
        )
        result = parser.getQueuedSenderComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is not None
        assert result.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"


class TestGetModeSwitchedAckRequest:
    """Tests for getModeSwitchedAckRequest (L2167-2173)."""

    def test_with_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-SWITCHED-ACK>
                <TIMEOUT>0.5</TIMEOUT>
            </MODE-SWITCHED-ACK>
            """
        )
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is not None
        assert result.getTimeout() is not None

    def test_without_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is None


class TestGetModeSwitchSenderComSpec:
    """Tests for getModeSwitchSenderComSpec (L2175-2180)."""

    def test_with_all_fields(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
            <MODE-SWITCHED-ACK>
                <TIMEOUT>1.0</TIMEOUT>
            </MODE-SWITCHED-ACK>
            <QUEUE-LENGTH>5</QUEUE-LENGTH>
            """,
            root_tag="MODE-SWITCH-SENDER-COM-SPEC",
        )
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getModeGroupRef() is not None
        assert result.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert result.getModeSwitchedAck() is not None
        assert result.getModeSwitchedAck().getTimeout() is not None
        assert result.getQueueLength() is not None

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="MODE-SWITCH-SENDER-COM-SPEC")
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getModeGroupRef() is None
        assert result.getModeSwitchedAck() is None
        assert result.getQueueLength() is None


class TestGetNvProvideComSpec:
    """Tests for getNvProvideComSpec (L2182-2188)."""

    def test_with_variable_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</VARIABLE-REF>',
            root_tag="NV-PROVIDE-COM-SPEC",
        )
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert result.getVariableRef() is not None
        assert result.getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert result.getVariableRef().getValue() == "/vdp/Var"

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="NV-PROVIDE-COM-SPEC")
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert result.getVariableRef() is None
        assert result.getRamBlockInitValue() is None
        assert result.getRomBlockInitValue() is None


class TestReadProvidedComSpec:
    """Tests for readProvidedComSpec (L2190-2204)."""

    @pytest.mark.parametrize("tag", [
        "QUEUED-SENDER-COM-SPEC",
        "MODE-SWITCH-SENDER-COM-SPEC",
    ])
    def test_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            f"""
            <PROVIDED-COM-SPECS>
                <{tag}></{tag}>
            </PROVIDED-COM-SPECS>
            """
        )
        parser.readProvidedComSpec(element, p_port)
        specs = p_port.getProvidedComSpecs()
        assert len(specs) == 1

    def test_nv_provide_branch_with_mock_parent(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        mock_parent = MagicMock()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <NV-PROVIDE-COM-SPEC></NV-PROVIDE-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        parser.readProvidedComSpec(element, mock_parent)
        assert mock_parent.addProvidedComSpec.called
        com_spec = mock_parent.addProvidedComSpec.call_args[0][0]
        assert com_spec is not None

    def test_unknown_branch_raises(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        with pytest.raises(ValueError):
            parser.readProvidedComSpec(element, p_port)

    def test_unknown_branch_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        warning_parser.readProvidedComSpec(element, p_port)
        assert len(p_port.getProvidedComSpecs()) == 0

    def test_empty_provided_com_specs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip("")
        parser.readProvidedComSpec(element, p_port)
        assert len(p_port.getProvidedComSpecs()) == 0
